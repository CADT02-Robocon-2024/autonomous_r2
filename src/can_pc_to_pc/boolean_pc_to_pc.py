import can as com

def converter(data):
    if data == True:
        return 0x01
    if data == False:
        return 0x00

def send_data_can(mid, data):
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x00 + mid)
    for i in range(3,6):
        m_data.append(converter(data))
    for i in range(6, 12):
        m_data.append(0x00)
    m_data.append(0x55)
    com.uca.frame_send(m_data)
    print("Data sent")

def receive_data_can():
    frame = com.uca.frame_receive()
    print("Data received")
    print(f"{frame}\n")