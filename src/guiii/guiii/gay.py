import customtkinter as ctk
import rclpy
from std_msgs.msg import Bool
from cadt02_interfaces.msg import ArduinoFeedback

rclpy.init()
node = rclpy.create_node('gui_publisher')

publisher_start = node.create_publisher(Bool, 'start', 10)
publisher_retry_ii = node.create_publisher(Bool, 'retry_ii', 10)
publisher_team_selected = node.create_publisher(ArduinoFeedback, 'team_selected', 10)

msg = ArduinoFeedback()


def publish_start_message(start):
    msg.start = start
    print("start")
    print(msg.start)
    publisher_team_selected.publish(msg)
    node.get_logger().info(f'Publishing start for {"Blue" if start else "Red"} Team: {msg.start}')

def publish_retry_ii_message(retry):
    msg.retry = retry
    publisher_team_selected.publish(msg)
    node.get_logger().info(f'Publishing retry II for {"Blue" if retry else "Red"} Team: {msg.retry}')

def publish_team_selected_message(team):
    msg.mode = team
    publisher_team_selected.publish(msg)
    node.get_logger().info(f'Publishing team selected: {"Blue" if team else "Red"} Team')

def start_red_clicked():
    publish_start_message(True)
    publish_team_selected_message(False)

def start_blue_clicked():
    publish_start_message(True)
    publish_team_selected_message(True)

def retry_ii_red_clicked():
    publish_retry_ii_message(True)
    publish_team_selected_message(False)

def retry_ii_blue_clicked():
    publish_retry_ii_message(True)
    publish_team_selected_message(True)

def select_red_team():
    publish_team_selected_message(False)
    show_red_team_buttons()

def select_blue_team():
    publish_team_selected_message(True)
    show_blue_team_buttons()

app = ctk.CTk()
app.title("CADT 02 ABU Robocon GUI")
app.geometry("600x400")

ctk.set_appearance_mode("dark")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

def show_team_buttons():
    publish_start_message(False)
    publish_retry_ii_message(False)
    for widget in main_frame.winfo_children():
        widget.destroy()

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    red_button = ctk.CTkButton(main_frame, text="Red Team", height=180, command=select_red_team, fg_color="red")
    red_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    blue_button = ctk.CTkButton(main_frame, text="Blue Team", height=180, command=select_blue_team, fg_color="blue")
    blue_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

def show_red_team_buttons():
    for widget in main_frame.winfo_children():
        widget.destroy()

    main_frame.grid_columnconfigure(0, weight=1)

    start_red_button = ctk.CTkButton(main_frame, text="Start", height=180, width=580, command=start_red_clicked, fg_color="red")
    start_red_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    retry_ii_red_button = ctk.CTkButton(main_frame, text="Retry II", height=180, width=580, command=retry_ii_red_clicked, fg_color="red")
    retry_ii_red_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    back_button = ctk.CTkButton(main_frame, text="Back", height=90, width=580, command=show_team_buttons)
    back_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

def show_blue_team_buttons():
    for widget in main_frame.winfo_children():
        widget.destroy()

    main_frame.grid_columnconfigure(0, weight=1)

    start_blue_button = ctk.CTkButton(main_frame, text="Start", height=180, width=580, command=start_blue_clicked, fg_color="blue")
    start_blue_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    retry_ii_blue_button = ctk.CTkButton(main_frame, text="Retry II", height=180, width=580, command=retry_ii_blue_clicked, fg_color="blue")
    retry_ii_blue_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    back_button = ctk.CTkButton(main_frame, text="Back", height=90, width=580, command=show_team_buttons)
    back_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

show_team_buttons()

app.mainloop()

node.destroy_node()
rclpy.shutdown()
