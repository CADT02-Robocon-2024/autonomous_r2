from movement.usbcan_adapter import UsbCanAdapter

uca = UsbCanAdapter()
uca.speed = 1000000
uca.adapter_init(device_port="/dev/ttyUSB0", baudrate=115200)

def read_from_port(ss):
    while True:
        print(uca.extract_data(uca.frame_receive()))


