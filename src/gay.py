import customtkinter as ctk
import rclpy
from geometry_msgs.msg import Twist, Vector3

# Initialize ROS node
rclpy.init()
node = rclpy.create_node('gui_publisher')

# ROS Publisher and Subscriber (placeholders)
publisher_distance = node.create_publisher(Twist, 'cmd_vel', 10)
subscriber_speed = node.create_subscription(Vector3, 'odometry', None, 10)  # Placeholder, actual callback needed

def publish_velocity_distance(vx, vy, omega):
    msg = Twist()
    msg.linear.x = vx
    msg.linear.y = vy
    msg.angular.z = omega
    publisher_distance.publish(msg)
    node.get_logger().info(f'Published distance command: linear.x={vx}, linear.y={vy}, angular.z={omega}')

# Initialize the main window
app = ctk.CTk()
app.title("CADT 02 ABU Robocon GUI")
app.geometry("1000x600")

# Set the appearance mode to dark
ctk.set_appearance_mode("dark")

# Configure the main window's grid to be responsive
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)

# Create sidebar frame
sidebar_frame = ctk.CTkFrame(app, width=200, corner_radius=10)
sidebar_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
sidebar_frame.grid_rowconfigure(5, weight=1)

# Create main content frame
main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

# Function to switch to the Home page
def show_home():
    home_button.configure(fg_color="blue")
    testing_button.configure(fg_color=("gray75", "gray25"))

    # Clear existing widgets in main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()
# Function to switch to the Testing page
def show_testing():
    home_button.configure(fg_color=("gray75", "gray25"))
    testing_button.configure(fg_color="blue")

    # Clear existing widgets in main_frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    create_testing_frame(main_frame, "Distance", [("X", "input here"), ("Y", "input here"), ("Omega", "input here")], 0, 0, publisher_distance)
    create_testing_frame(main_frame, "Speed", [("Vx", "input here"), ("Vy", "input here"), ("Omega", "input here")], 0, 1, subscriber_speed)
    create_simple_testing_frame(main_frame, "Grab Ball Testing", ["Grab"], 1, 0)
    create_simple_testing_frame(main_frame, "Rail", ["Up", "Down"], 1, 1)
    create_simple_testing_frame(main_frame, "Flip", ["Flip", "Flip Back"], 2, 0)

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
            vx = float(entry_widgets[0].get())  # Assuming entry_widgets[0] refers to X input field
            vy = float(entry_widgets[1].get())  # Assuming entry_widgets[1] refers to Y input field
            omega = float(entry_widgets[2].get())  # Assuming entry_widgets[2] refers to Omega input field
            omega_rad = omega * (3.14159 / 180)
            publish_velocity_distance(vx, vy, omega_rad)
        # You can add more conditions for different publishers/subscribers if needed

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Function to create simple testing frame
def create_simple_testing_frame(parent, title, buttons, row, column):
    frame = ctk.CTkFrame(parent)
    frame.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")
    frame.grid_columnconfigure((0, 1), weight=1)

    label = ctk.CTkLabel(frame, text=title, font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=len(buttons), pady=10)

    for i, button in enumerate(buttons):
        btn = ctk.CTkButton(frame, text=button)
        btn.grid(row=1, column=i, padx=10, pady=10, sticky="ew")


# Add buttons to the sidebar
home_button = ctk.CTkButton(sidebar_frame, text="Home", command=show_home)
home_button.grid(row=0, column=0, pady=10, padx=10)

testing_button = ctk.CTkButton(sidebar_frame, text="Testing", command=show_testing)
testing_button.grid(row=1, column=0, pady=10, padx=10)

# Run the main loop
app.mainloop()

# Shutdown ROS when GUI closes
node.destroy_node()
rclpy.shutdown()
