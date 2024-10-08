import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor
import gym
from gym import spaces
from gym.core import ObservationWrapper
import numpy as np
import torch
from torchvision.transforms import transforms
import pyrealsense2 as rs
import cv2
from ultralytics import YOLO
import json
import os

class Observation:
    def __init__(self, silo_states, ball_color, team_color):
        self.silo_states = silo_states
        self.ball_color = ball_color
        self.team_color = team_color

    def to_json(self):
        return json.dumps({
            "silo_states": self.silo_states,
            "ball_color": self.ball_color,
            "team_color": self.team_color
        })

class Reward:
    def __init__(self, reward):
        self.reward = reward

    def to_json(self):
        return json.dumps({
            "reward": self.reward
        })

class ObjectDetectionEnv(gym.Env):
    def __init__(self, model_path):
        super(ObjectDetectionEnv, self).__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = YOLO(model_path)
        self.silo_states = [""] * 5  # Stores the balls in each of the 5 silos
        self.ball_colors = ["blue", "purple", "red"]
        self.team_color = None  # Current team color (0 for red, 1 for blue)
        self.game_over = False

        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((640, 480)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize to [0, 1]
        ])

        self.action_space = spaces.Discrete(5)  # Number of silos
        self.observation_space = spaces.Dict({
            "silo_states": spaces.MultiDiscrete([13] * 5),  # Each silo can have up to 3 balls of 3 types
            "ball_color": spaces.Discrete(3),  # Blue, purple, red
            "team_color": spaces.Discrete(2)   # Red or blue
        })

        # Initialize RealSense pipeline
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(self.config)

    def reset(self, **kwargs):
        # Reset environment to initial state
        self.silo_states = [""] * 5
        self.ball_color = np.random.choice(self.ball_colors)  # Randomly assign ball color
        self.team_color = np.random.choice([0, 1])  # Randomly assign team color (0 for red, 1 for blue)
        self.game_over = False
        return self._get_observation(), None

    def step(self, action):
        # Execute action and return new state, reward, and done flag
        if self.game_over:
            raise ValueError("Episode is already done. Please reset the environment.")

        # Perform action (place ball in silo)
        self.silo_states[action] += self.ball_color[0].upper()  # Add first letter of ball color

        # Perform live object detection
        detections = self.perform_object_detection()

        # Update state with information about detected objects
        self.update_state_with_detections(detections)

        # Check if any silo is full
        if any(len(silo) >= 3 for silo in self.silo_states):
            # Check for winning condition
            if sum(len(silo) >= 3 for silo in self.silo_states) >= 3:
                # Team wins if at least 3 silos are filled
                reward = 100  # High reward for winning
                self.game_over = True
            else:
                # Count balls in filled silos as points
                reward = sum(len(silo) >= 3 for silo in self.silo_states) * 30
                self.game_over = True
        else:
            reward = 0  # No reward if the game is still ongoing

        return self._get_observation(), reward, self.game_over, {}

    def perform_object_detection(self):
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        if not color_frame or not depth_frame:
            return []

        color_image = np.asanyarray(color_frame.get_data())

        # Perform object detection using the model
        results = self.model(color_image)

        # Process detections and extract relevant information
        detections_list = []
        for result in results:
            for det in result.boxes:  # Assuming 'boxes' is the attribute containing detection boxes
                bbox = det.xyxy[0].cpu().numpy().astype(int)  # Get bounding box coordinates
                confidence = det.conf[0].item()  # Get confidence
                label = det.cls[0].item()  # Get class label
                center_x = int((bbox[0] + bbox[2]) / 2)
                center_y = int((bbox[1] + bbox[3]) / 2)
                depth_value = depth_frame.get_distance(center_x, center_y)

                detections_list.append({
                    "label": label,
                    "confidence": confidence,
                    "bbox": bbox,
                    "depth": depth_value
                })

        return detections_list

    def update_state_with_detections(self, detections):
        for detection in detections:
            label = detection["label"]
            confidence = detection["confidence"]

            if label == 0 and confidence > 0.5:  # Assuming 0 is the label for blue ball
                self.ball_color = "blue"
            elif label == 1 and confidence > 0.5:  # Assuming 1 is the label for purple ball
                self.ball_color = "purple"
            elif label == 2 and confidence > 0.5:  # Assuming 2 is the label for red ball
                self.ball_color = "red"
            elif label == 3 and confidence > 0.5:  # Assuming 3 is the label for "NULL"
                # Check if ball is in a silo
                for i, silo_bbox in enumerate(self.get_silo_bboxes()):
                    if self.check_overlap(detection["bbox"], silo_bbox):
                        if self.silo_states[i]:
                            self.silo_states[i] = self.silo_states[i][:-1]  # Remove last ball
                        break

    def _get_observation(self):
        # Return current observation (state of the game)
        observation = {
            "silo_states": [self._encode_silo(silo) for silo in self.silo_states],
            "ball_color": self.ball_colors.index(self.ball_color),
            "team_color": self.team_color
        }
        return observation

    def _encode_silo(self, silo):
        # Encode silo state as a discrete number for the observation space
        encoding = {"": 0, "B": 1, "P": 2, "R": 3, "BB": 4, "BP": 5, "BR": 6, "PB": 7, "PP": 8, "PR": 9, "RB": 10, "RP": 11, "RR": 12}
        return encoding.get(silo, 0)

    def render(self, mode='human'):
        if mode == 'human':
            while True:
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()
                if not color_frame:
                    continue

                frame = np.asanyarray(color_frame.get_data())

                with torch.no_grad():
                    results = self.model(frame)

                for result in results:
                    for det in result.boxes:
                        bbox = det.xyxy[0].cpu().numpy().astype(int)
                        label = int(det.cls[0].item())
                        confidence = det.conf[0].item()

                        if confidence > 0.5:
                            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                            cv2.putText(frame, str(label), (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                cv2.imshow('Object Detection', frame)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break

            cv2.destroyAllWindows()

        elif mode == 'rgb_array':
            # Return the current frame as an RGB array (optional)
            # You may implement this if you want to render the environment in a custom way
            pass

    def get_silo_bboxes(self):
        # Placeholder function to return bounding boxes for silos
        return [np.array([i * 100, 0, (i + 1) * 100, 480]) for i in range(5)]

    def check_overlap(self, bbox1, bbox2):
        x1_max = max(bbox1[0], bbox2[0])
        y1_max = max(bbox1[1], bbox2[1])
        x2_min = min(bbox1[2], bbox2[2])
        y2_min = min(bbox1[3], bbox2[3])
        return x1_max < x2_min and y1_max < y2_min

class FlattenDictWrapper(ObservationWrapper):
    def __init__(self, env):
        super(FlattenDictWrapper, self).__init__(env)
        self.observation_space = self._flatten_observation_space(env.observation_space)

    def _flatten_observation_space(self, space):
        if isinstance(space, spaces.Dict):
            flat_dims = sum([np.prod(space.spaces[key].shape) for key in space.spaces])
            return spaces.Box(low=np.zeros(int(flat_dims)), high=np.inf, shape=(int(flat_dims),), dtype=np.float32)
        else:
            raise NotImplementedError("Unsupported observation space type")

    def observation(self, observation):
        if isinstance(observation, dict):
            return np.concatenate([observation[key].flatten() for key in observation])
        else:
            return observation

class ObjectDetectionNode(Node):
    def __init__(self):
        # Initialize node and environment
        super().__init__('reinforcement_r2')
        self.model_path = "/home/cadt-02/Downloads/model_- 6 may 2024 19_25.pt"
        
        # Set up the environment with Monitor for logging and FlattenDictWrapper for observation space
        env = ObjectDetectionEnv(self.model_path)
        env = FlattenDictWrapper(env)
        env = Monitor(env, "./dqn_logs/monitor.csv")
        self.env = DummyVecEnv([lambda: env])
        
        self.model = DQN("MlpPolicy", self.env, verbose=1, tensorboard_log="./dqn_logs/")

        # Create publishers for observations and rewards
        self.observation_publisher = self.create_publisher(String, 'observation_topic', 10)
        self.reward_publisher = self.create_publisher(String, 'reward_topic', 10)

        # Set up timer for publishing observations and rewards
        self.timer_period = 0.5  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        # Initialize variables for training loop
        self.episode_count = 0
        self.max_episodes = 1000  # Define maximum number of episodes for training

    def timer_callback(self):
        if self.episode_count >= self.max_episodes:
            self.get_logger().info('Training complete!')
            self.model.save("/home/cadt-02/Object-Detection/dqn_logs")
            return

        # Reset environment for each episode
        observation = self.env.reset()
        done = False
        while not done:
            # Publish observation
            observation_json = {
                "silo_states": observation["silo_states"],
                "ball_color": int(observation["ball_color"]),
                "team_color": int(observation["team_color"])
            }

            msg = String()
            msg.data = json.dumps(observation_json)
            self.observation_publisher.publish(msg)

            # Predict action and step through environment
            action, _states = self.model.predict(observation)
            next_observation, reward, done, _ = self.env.step(action)

            # Publish reward
            reward_json = {"reward": float(reward)}
            msg = String()
            msg.data = json.dumps(reward_json)
            self.reward_publisher.publish(msg)

            # Log reward to TensorBoard
            self.model.get_writer().add_scalar("reward", reward, self.episode_count)

            # Update observation for next step
            observation = next_observation

        self.episode_count += 1

def main(args=None):
    rclpy.init(args=args)
    node = ObjectDetectionNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
