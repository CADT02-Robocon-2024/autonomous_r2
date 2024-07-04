import customtkinter as ctk
import rclpy
from rclpy.node import Node
from gui_inter.msg import Hello

# Initialize the ROS node
rclpy.init()
node = rclpy.create_node('gui_node')

# Define ROS publisher
publisher = node.create_publisher(Hello, 'team_selection', 10)

app = ctk.CTk()
app.title("CADT 02 ABU Robocon GUI")
app.geometry("1000x600")

ctk.set_appearance_mode("dark")

team_selected = False
start = "No"
retry_ii = 0

def publish_ros_message():
    global team_selected, start, retry_ii
    
    # Create and publish the custom message
    msg = Hello()
    msg.team_selected = team_selected
    msg.start = start
    msg.retry_ii = retry_ii

    publisher.publish(msg)
    node.get_logger().info(f'Publishing team_selected: {msg.team_selected}, start: {msg.start}, retry_ii: {msg.retry_ii}')

def red_team_clicked():
    global team_selected, start, retry_ii
    team_selected = False
    start = "No"
    retry_ii = 0
    start_button.configure(state="disabled")
    retry_ii_button.configure(state="disabled")
    publish_ros_message()

def blue_team_clicked():
    global team_selected, start, retry_ii
    team_selected = True
    start = "No"
    retry_ii = 0
    start_button.configure(state="normal")
    retry_ii_button.configure(state="normal")
    publish_ros_message()

def start_clicked():
    global start
    start = "Yes"
    publish_ros_message()

def retry_ii_clicked():
    global retry_ii
    retry_ii = 1
    publish_ros_message()

top_frame = ctk.CTkFrame(app)
top_frame.grid(row=0, column=0, sticky="nsew")

title_label = ctk.CTkLabel(top_frame, text="Team", font=("Helvetica", 24, "underline"))
title_label.grid(pady=10, padx=450)

button_frame = ctk.CTkFrame(top_frame)
button_frame.grid(pady=20)

red_team_button = ctk.CTkButton(button_frame, text="Red Team", fg_color="grey", height=50, width=200, command=red_team_clicked)
red_team_button.grid(row=0, column=0, padx=10, sticky="ew")

blue_team_button = ctk.CTkButton(button_frame, text="Blue Team", fg_color="grey", height=50, width=200, command=blue_team_clicked)
blue_team_button.grid(row=0, column=1, padx=10, sticky="ew")

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

start_retry_frame = ctk.CTkFrame(app)
start_retry_frame.grid(row=1, column=0, sticky="nsew")

start_button = ctk.CTkButton(start_retry_frame, text="Start", height=200, width=400, state="disabled", command=start_clicked)
start_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

retry_ii_button = ctk.CTkButton(start_retry_frame, text="Retry II", height=200, width=400, state="disabled", command=retry_ii_clicked)
retry_ii_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

start_retry_frame.grid_columnconfigure(0, weight=1)
start_retry_frame.grid_rowconfigure(0, weight=1)
start_retry_frame.grid_rowconfigure(1, weight=1)

app.mainloop()

# Shutdown the ROS node when the app closes
rclpy.shutdown()
