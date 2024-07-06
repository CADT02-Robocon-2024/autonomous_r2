# import customtkinter as ctk
# import rclpy
# from gui_inter.msg import Hello

# rclpy.init()
# node = rclpy.create_node('gui_node')

# publisher_hello = node.create_publisher(Hello, 'team_selection', 10)

# app = ctk.CTk()
# app.title("CADT 02 ABU Robocon GUI")
# app.geometry("1000x600")

# ctk.set_appearance_mode("dark")

# team_selected = False
# start = False
# retry_ii = False

# def publish_hello_message():
#     global team_selected, start, retry_ii
    
#     msg = Hello()
#     msg.team_selected = team_selected
#     msg.start = start
#     msg.retry_ii = retry_ii

#     publisher_hello.publish(msg)
#     node.get_logger().info(f'Publishing team_selected: {msg.team_selected}, start: {msg.start}, retry_ii: {msg.retry_ii}')

# def red_team_clicked():
#     global team_selected
#     team_selected = False
#     publish_hello_message()

# def blue_team_clicked():
#     global team_selected
#     team_selected = True
#     publish_hello_message()

# def start_clicked():
#     global start
#     start = True
#     publish_hello_message()

# def retry_ii_clicked():
#     global retry_ii
#     retry_ii = True
#     publish_hello_message()

# top_frame = ctk.CTkFrame(app)
# top_frame.grid(row=0, column=0, sticky="nsew")

# title_label = ctk.CTkLabel(top_frame, text="Team", font=("Helvetica", 24, "underline"))
# title_label.grid(pady=10, padx=450)

# button_frame = ctk.CTkFrame(top_frame)
# button_frame.grid(pady=20)

# red_team_button = ctk.CTkButton(button_frame, text="Red Team", fg_color="grey", height=50, width=200, command=red_team_clicked)
# red_team_button.grid(row=0, column=0, padx=10, sticky="ew")

# blue_team_button = ctk.CTkButton(button_frame, text="Blue Team", fg_color="grey", height=50, width=200, command=blue_team_clicked)
# blue_team_button.grid(row=0, column=1, padx=10, sticky="ew")

# button_frame.grid_columnconfigure(0, weight=1)
# button_frame.grid_columnconfigure(1, weight=1)

# start_retry_frame = ctk.CTkFrame(app)
# start_retry_frame.grid(row=1, column=0, sticky="nsew")

# start_button = ctk.CTkButton(start_retry_frame, text="Start", height=200, width=400, state="disabled", command=start_clicked)
# start_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# retry_ii_button = ctk.CTkButton(start_retry_frame, text="Retry II", height=200, width=400, state="disabled", command=retry_ii_clicked)
# retry_ii_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# app.grid_columnconfigure(0, weight=1)
# app.grid_rowconfigure(0, weight=1)
# app.grid_rowconfigure(1, weight=1)

# start_retry_frame.grid_columnconfigure(0, weight=1)
# start_retry_frame.grid_rowconfigure(0, weight=1)
# start_retry_frame.grid_rowconfigure(1, weight=1)

# app.mainloop()

# rclpy.shutdown()


# Note
# note
# note

# 2nd method 

# import customtkinter as ctk
# import rclpy
# from std_msgs.msg import Bool

# rclpy.init()
# node = rclpy.create_node('gui_node')

# publisher_start = node.create_publisher(Bool, 'start', 10)
# publisher_retry_ii = node.create_publisher(Bool, 'retry_ii', 10)

# app = ctk.CTk()
# app.title("CADT 02 ABU Robocon GUI")
# app.geometry("1000x600")

# ctk.set_appearance_mode("dark")

# def publish_start_message(is_blue):
#     msg = Bool()
#     msg.data = is_blue
#     publisher_start.publish(msg)
#     node.get_logger().info(f'Publishing start for {"Blue" if is_blue else "Red"} Team: {msg.data}')

# def publish_retry_ii_message(is_blue):
#     msg = Bool()
#     msg.data = is_blue
#     publisher_retry_ii.publish(msg)
#     node.get_logger().info(f'Publishing retry II for {"Blue" if is_blue else "Red"} Team: {msg.data}')

# def start_red_clicked():
#     publish_start_message(False)

# def start_blue_clicked():
#     publish_start_message(True)

# def retry_ii_red_clicked():
#     publish_retry_ii_message(False)

# def retry_ii_blue_clicked():
#     publish_retry_ii_message(True)

# start_retry_frame = ctk.CTkFrame(app)
# start_retry_frame.grid(row=0, column=0, sticky="nsew")

# red_label = ctk.CTkLabel(start_retry_frame, text="Red Team", font=("Helvetica", 20))
# red_label.grid(row=0, column=0, pady=10, padx=20)

# start_red_button = ctk.CTkButton(start_retry_frame, text="Start", height=180, width=200, command=start_red_clicked)
# start_red_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# retry_ii_red_button = ctk.CTkButton(start_retry_frame, text="Retry II", height=180, width=200, command=retry_ii_red_clicked)
# retry_ii_red_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# blue_label = ctk.CTkLabel(start_retry_frame, text="Blue Team", font=("Helvetica", 20))
# blue_label.grid(row=0, column=1, pady=10, padx=20)

# start_blue_button = ctk.CTkButton(start_retry_frame, text="Start", height=180, width=200, command=start_blue_clicked)
# start_blue_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# retry_ii_blue_button = ctk.CTkButton(start_retry_frame, text="Retry II", height=180, width=200, command=retry_ii_blue_clicked)
# retry_ii_blue_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# app.grid_columnconfigure(0, weight=1)
# app.grid_rowconfigure(0, weight=1)

# start_retry_frame.grid_columnconfigure(0, weight=1)
# start_retry_frame.grid_columnconfigure(1, weight=1)
# start_retry_frame.grid_rowconfigure(0, weight=1)
# start_retry_frame.grid_rowconfigure(1, weight=1)
# start_retry_frame.grid_rowconfigure(2, weight=1)

# app.mainloop()

# rclpy.shutdown()







# note
# note
# note

# for Tesing all the function



import customtkinter as ctk
import rclpy
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Bool

rclpy.init()
node = rclpy.create_node('gui_publisher')

publisher_distance = node.create_publisher(Twist, 'cmd_vel', 10)
publisher_speed = node.create_publisher(Vector3, 'odometry', 10)
publisher_rail = node.create_publisher(Bool, 'rail', 10)
publisher_grab = node.create_publisher(Bool, 'grab', 10)
publisher_flip = node.create_publisher(Bool, 'flip', 10)
publisher_start = node.create_publisher(Bool, 'start', 10)
publisher_retry_ii = node.create_publisher(Bool, 'retry_ii', 10)

def publish_velocity_distance(vx, vy, omega):
    msg = Twist()
    msg.linear.x = vx
    msg.linear.y = vy
    msg.angular.z = omega
    publisher_distance.publish(msg)
    node.get_logger().info(f'Published distance command: linear.x={vx}, linear.y={vy}, angular.z={omega}')

def publish_speed(vx, vy, omega):
    msg = Vector3()
    msg.x = vx
    msg.y = vy
    msg.z = omega
    publisher_speed.publish(msg)
    node.get_logger().info(f'Published speed command: Vx={msg.x}, Vy={msg.y}, Omega={msg.z}')

def publish_rail(up):
    msg = Bool()
    msg.data = up
    publisher_rail.publish(msg)
    node.get_logger().info(f'Published rail command: {"Up" if up else "Down"}')

def publish_grab(grab):
    msg = Bool()
    msg.data = grab
    publisher_grab.publish(msg)
    node.get_logger().info(f'Published grab command: {"Grab" if grab else "Release"}')

def publish_flip(flip):
    msg = Bool()
    msg.data = flip
    publisher_flip.publish(msg)
    node.get_logger().info(f'Published flip command: {"Flip" if flip else "Flip Back"}')

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

app = ctk.CTk()
app.title("CADT 02 ABU Robocon GUI")
app.geometry("1000x600")

ctk.set_appearance_mode("dark")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)

sidebar_frame = ctk.CTkFrame(app, width=200, corner_radius=10)
sidebar_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
sidebar_frame.grid_rowconfigure(5, weight=1)

main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

def show_home():
    home_button.configure(fg_color="blue")
    testing_button.configure(fg_color=("gray75", "gray25"))

    for widget in main_frame.winfo_children():
        widget.destroy()

    start_retry_frame = ctk.CTkFrame(main_frame)
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

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)

    start_retry_frame.grid_columnconfigure(0, weight=1)
    start_retry_frame.grid_columnconfigure(1, weight=1)
    start_retry_frame.grid_rowconfigure(0, weight=1)
    start_retry_frame.grid_rowconfigure(1, weight=1)
    start_retry_frame.grid_rowconfigure(2, weight=1)

# Function to switch to the Testing page
def show_testing():
    home_button.configure(fg_color=("gray75", "gray25"))
    testing_button.configure(fg_color="blue")

    # Clear existing widgets in main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    create_testing_frame(main_frame, "Distance", [("X", "input here"), ("Y", "input here"), ("Omega", "input here")], 0, 0, publisher_distance)
    create_testing_frame(main_frame, "Speed", [("Vx", "input here"), ("Vy", "input here"), ("Omega", "input here")], 0, 1, publisher_speed)
    create_simple_testing_frame(main_frame, "Grab Ball Testing", [("Grab", True), ("Release", False)], 1, 0, publish_grab)
    create_simple_testing_frame(main_frame, "Rail", [("Up", True), ("Down", False)], 1, 1, publish_rail)
    create_simple_testing_frame(main_frame, "Flip", [("Flip", True), ("Flip Back", False)], 2, 0, publish_flip)

# Function to create a testing frame
def create_testing_frame(parent, title, commands, row, column, publisher):
    frame = ctk.CTkFrame(parent)
    frame.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")
    frame.grid_columnconfigure(1, weight=1)

    label = ctk.CTkLabel(frame, text=title, font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    entry_widgets = []  # List to store entry widgets

    for i, (cmd, placeholder) in enumerate(commands):
        cmd_label = ctk.CTkLabel(frame, text=cmd, font=("Arial", 14, "bold"))
        cmd_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e")

        entry = ctk.CTkEntry(frame, placeholder_text=placeholder)
        entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="we")

        entry_widgets.append(entry)  # Store the entry widget

    send_button = ctk.CTkButton(frame, text="Send", command=lambda: send_command(entry_widgets, publisher))
    send_button.grid(row=len(commands)+1, column=1, pady=10, padx=10, sticky="e")

def send_command(entry_widgets, publisher):
    try:
        if publisher == publisher_distance:
            vx = float(entry_widgets[0].get())
            vy = float(entry_widgets[1].get())  
            omega = float(entry_widgets[2].get())  
            omega_rad = omega * (3.14159 / 180)
            publish_velocity_distance(vx, vy, omega_rad)
        elif publisher == publisher_speed:
            vx = float(entry_widgets[0].get())  
            vy = float(entry_widgets[1].get())  
            omega = float(entry_widgets[2].get()) 
            publish_speed(vx, vy, omega)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def create_simple_testing_frame(parent, title, buttons, row, column, publisher):
    frame = ctk.CTkFrame(parent)
    frame.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")
    frame.grid_columnconfigure((0, 1), weight=1)

    label = ctk.CTkLabel(frame, text=title, font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=len(buttons), pady=10)

    for i, (button, value) in enumerate(buttons):
        btn = ctk.CTkButton(frame, text=button, command=lambda v=value: publisher(v))
        btn.grid(row=1, column=i, padx=10, pady=10, sticky="ew")

home_button = ctk.CTkButton(sidebar_frame, text="Home", command=show_home)
home_button.grid(row=0, column=0, pady=10, padx=10)

testing_button = ctk.CTkButton(sidebar_frame, text="Testing", command=show_testing)
testing_button.grid(row=1, column=0, pady=10, padx=10)

app.mainloop()

node.destroy_node()
rclpy.shutdown()
