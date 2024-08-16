#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Bool
from cadt02_interfaces.msg import Silo


class BallHandlingNode(Node):
    def init(self):
        super().init('ball_handling_node')

        self.subscription = self.create_subscription(
            Bool,
            'ball_caught',
            self.ball_caught_callback,
            10)
        self.publisher = self.create_publisher(Silo, 'silo_num', 10)
        self.silo = Silo()

        # Initialize silo states
        self.num_silos = 5
        self.silo_capacity = 3
        self.silo_states = [0] * self.num_silos  # Initialize silos with zero balls

    def ball_caught_callback(self, msg):
        if msg.data:
            silo_index = self.find_available_silo()
            if silo_index is not None:
                self.silo_states[silo_index] += 1
                self.publisher.publish(Int32(data=silo_index))
                self.get_logger().info(f'Ball placed in silo {silo_index}.')
            else:
                self.get_logger().warn('All silos are full! Cannot place the ball.')

    def find_available_silo(self):
        for index, count in enumerate(self.silo_states):
            if count < self.silo_capacity:
                return index
        return None

def main(args=None):
    rclpy.init(args=args)
    ball_handling_node = BallHandlingNode()
    rclpy.spin(ball_handling_node)
    ball_handling_node.destroy_node()
    rclpy.shutdown()

if name == 'main':
    main()