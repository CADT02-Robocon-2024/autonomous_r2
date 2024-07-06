import customtkinter as ctk
import rclpy
from std_msgs.msg import Bool

rclpy.init()
node = rclpy.create_node('gui_node')

publisher_start = node.create_publisher(Bool, 'start', 10)
publisher_retry_ii = node.create_publisher(Bool, 'retry_ii', 10)

app = ctk.CTk()
app.title("CADT 02 ABU Robocon GUI")
app.geometry("1000x600")

ctk.set_appearance_mode("dark")

def publish_start_message(is_blue):
    msg = Bool()
    msg.data = is_blue
    publisher_start.publish(msg)
    node.get_logger().info(f'Publishing start for {"Blue" if is_blue else "Red"} Team: {msg.data}')

def publish_retry_ii_message(is_blue):
    msg = Bool()
    msg.data = is_blue
    publisher_retry_ii.publish(msg)
    node.get_logger().info(f'Publishing retry II for {"Blue" if is_blue else "Red"} Team: {msg.data}')

def start_red_clicked():
    publish_start_message(False)

def start_blue_clicked():
    publish_start_message(True)

def retry_ii_red_clicked():
    publish_retry_ii_message(False)

def retry_ii_blue_clicked():
    publish_retry_ii_message(True)

start_retry_frame = ctk.CTkFrame(app)
start_retry_frame.grid(row=0, column=0, sticky="nsew")

red_label = ctk.CTkLabel(start_retry_frame, text="Red Team", font=("Helvetica", 20))
red_label.grid(row=0, column=0, pady=10, padx=20)

start_red_button = ctk.CTkButton(start_retry_frame, text="Start", height=180, width=200, command=start_red_clicked)
start_red_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

retry_ii_red_button = ctk.CTkButton(start_retry_frame, text="Retry II", height=180, width=200, command=retry_ii_red_clicked)
retry_ii_red_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

blue_label = ctk.CTkLabel(start_retry_frame, text="Blue Team", font=("Helvetica", 20))
blue_label.grid(row=0, column=1, pady=10, padx=20)

start_blue_button = ctk.CTkButton(start_retry_frame, text="Start", height=180, width=200, command=start_blue_clicked)
start_blue_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

retry_ii_blue_button = ctk.CTkButton(start_retry_frame, text="Retry II", height=180, width=200, command=retry_ii_blue_clicked)
retry_ii_blue_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

start_retry_frame.grid_columnconfigure(0, weight=1)
start_retry_frame.grid_columnconfigure(1, weight=1)
start_retry_frame.grid_rowconfigure(0, weight=1)
start_retry_frame.grid_rowconfigure(1, weight=1)
start_retry_frame.grid_rowconfigure(2, weight=1)

app.mainloop()

rclpy.shutdown()
