#!/usr/bin/env python3

import inspect
import rclpy
from rclpy.node import Node
import math
from cadt02_interfaces.msg import SmartDriver, MotorFeedback, Silo
from std_msgs.msg import Float32
import can
import subprocess
import struct
import psutil
import threading
import os
import movement.can as com

def set_thread_priority():
    p = psutil.Process(os.getpid())
    try:
        p.nice(-20)  # Unix-based systems highest priority
        print("Priority set successfully")
    except psutil.AccessDenied as e:
        print(f"Failed to set thread priority due to permission error: {e}")
    except Exception as e:
        print(f"Failed to set thread priority: {e}")

class MotorCommandNode(Node):

    def __init__(self):
        super().__init__('motor_command_node')
        
        cmd = ["ip", "link", "show", "can0"]
        
        result = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        
        if b"state UP" in result.stdout:
            print("CAN interface is already up")
        else:
            cmd = ["sudo", "ip", "link", "set", "can0", "up", "type", "can", "bitrate", "1000000"]
            
            result = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            
            if result.returncode == 0:
                print("CAN interface is up")
            else:
                print("CAN failed to setup")

        self.subscriber = self.create_subscription(SmartDriver, '/publish_motor', self.callback, 1000) #topic to control the motor with smart driver
        self.encoder_publisher = self.create_publisher(MotorFeedback, 'motor_feedback', 10) #publish the feedbacks from the smart driver
        self.silo_publisher = self.create_publisher(Silo, 'silo_num', 10) #get the silo number from pc 2 via can usb
        self.range_pub = self.create_publisher(Float32, '/y_range', 10) # publish the range from the range finder TOF
 
        self.bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)
        
        self.canMsgData = [0, 0, 0, 0, 0, 0, 0, 0]

        # Use a separate thread to handle CAN message reception
        self.can_receive_thread = threading.Thread(target=self.smart_driver_feedback)
        self.can_receive_thread.daemon = True
        self.can_receive_thread.start()

        ##open for silo feedback
        self.silo_receive_thread = threading.Thread(target=self.silo_feedback)
        self.silo_receive_thread.daemon = True
        self.silo_receive_thread.start()
        
        self.timer = self.create_timer(0.1, self.get_dist)
        
        # set_thread_priority()  # Set the thread priority here

        self.feed_back = MotorFeedback()
        self.silo = Silo()
        
        self.tof = Float32()
        
    # this sends the command to the smart driver to control the gripper flip
    def callback(self, msg):
        if msg.motor_id == 7:
            self.solenoid_control(msg.motor_id, msg.goal)
        else:
            # msg.stop = True
            print("id:", msg.motor_id, "position:", msg.goal, "stop", msg.stop,)
            self.canMsgData[0] = (
                msg.speedmode +
                (msg.stop << 1) +
                (msg.reset << 2) +
                (msg.voltagemode << 3)
            )
            
            goal_bytes = struct.pack("<f", msg.goal)
            
            self.canMsgData[2:6] = goal_bytes
            
            can_msg = can.Message(arbitration_id=msg.motor_id, data=self.canMsgData, is_extended_id=False)
            try:
                self.bus.send(can_msg)
                print("Message sent on {}".format(self.bus.channel_info))
            except can.CanError:
                print("Message NOT sent")
    
    # control the solenoid vai can usb to arduino
    def solenoid_control(self, mid, solenoid):
        print("id:", mid, "solenoid:", solenoid)
        if solenoid == 0.0:
            boolean_data = 0x00
        else:
            boolean_data = 0x01
        self.canMsgData[0] = boolean_data
        print("canMsgData:", self.canMsgData)

        can_msg = can.Message(arbitration_id=mid, data=self.canMsgData, is_extended_id=False)
        try:
            self.bus.send(can_msg)
            print("Solenoid sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")

    # get motor feedback from the smart driver
    def smart_driver_feedback(self):
        while rclpy.ok():
            try:
                data = self.bus.recv() 
                # print(data.arbitration_id)
                if data.arbitration_id == 254:
                    self.feed_back.motor_id = data.arbitration_id
                    self.feed_back.speed = struct.unpack("<f", bytes(data.data[4:8]))[0]
                    self.feed_back.position = struct.unpack("<f", bytes(data.data[0:4]))[0]
                    self.encoder_publisher.publish(self.feed_back)
            except can.CanError as e:
                self.get_logger().error(f"CAN error: {e}")
    
    #get distance from the range finder
    def get_dist(self):
        data = self.bus.recv()
        # print("Raw data")
        # print(data)
        print(data.arbitration_id)
        if data.arbitration_id == 516:
            print(f"{data.arbitration_id} In range")
            # self.speed = struct.unpack("<f", bytes(data.data[4:8]))[0]
            # self.distance = struct.unpack("<f", bytes(data.data[0:2]))[0]
            first_three_bytes = data.data[:3]
            distance = struct.unpack('<I', first_three_bytes + b'\x00')[0]
            print(data.data)
            signal = data.data[4]
            print("Signal: ", signal)
            # self.tof.data = distance
            # print("Speed: ", self.recv.speed)
            print("Distance: ", distance)
            self.range_pub.publish(self.tof)
        elif data.arbitration_id == 518:
            print(f"{data.arbitration_id} In range")
            # self.speed = struct.unpack("<f", bytes(data.data[4:8]))[0]
            # self.distance = struct.unpack("<f", bytes(data.data[0:2]))[0]
            first_three_bytes = data.data[:3]
            distance = struct.unpack('<I', first_three_bytes + b'\x00')[0]
            print(data.data)
            signal = data.data[4]
            print("Signal: ", signal)
            # self.tof.data = distance
            # print("Speed: ", self.recv.speed)
            print("Distance: ", distance)
            self.range_pub.publish(self.tof)

        
    #get the silo number from the pc 2
    def silo_feedback(self):
        while rclpy.ok():
            # print("hello")
            com.uca.frame_receive() 
            frame_can = com.uca.extract_data(com.uca.frame)
            id = int(frame_can.get('frame_id'), 16)
            data = frame_can['data']
            print(frame_can) 
            if id == 8:
                self.silo.silo = int(data[1])
                self.silo_publisher.publish(self.silo) 
    def range_callback(self, msg):
        print(f"Received distance: {msg.data}")
        
    

def main(args=None):
    rclpy.init(args=args)

    motor_command_node = MotorCommandNode()

    rclpy.spin(motor_command_node)

    motor_command_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
