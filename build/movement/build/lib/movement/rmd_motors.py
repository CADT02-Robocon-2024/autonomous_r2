from movement.usbcan_adapter import UsbCanAdapter

uca = UsbCanAdapter()
uca.speed = 1000000
uca.adapter_init(device_port="/dev/ttyUSB1", baudrate=115200)

def ratio(mid, ang, velo):
    if mid == 1:
        ang *= 6.0
        velo *= 6.0
    elif mid == 2:
        ang *= 6.0
        velo *= 6.0
    elif mid == 3:
        ang *= 6.0
        velo *= 6.0
    elif mid == 4:
        ang *= 6.0
        velo *= 6.0
    elif mid == 5:
        ang *= 9.0
        velo *= 9.0
    elif mid == 6:
        ang *= 9.0
        velo *= 9.0
    else:
        ang *= 30.0
        velo *= 30.0
    return int(ang * 100), int(velo * 100)

def int_byte(int_data):
    return int_data & 0xFF


def run_speed(mid, velo):
    result = 0
    # chsum = 0
    degree, speed = ratio(mid, 0, velo)
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x40 + mid)
    m_data.append(0x01)
    m_data.append(0xA2)
    m_data.append(0x00)
    m_data.append(0x00)
    m_data.append(0x00)
    for i in range(8, 12):
        m_data.append(int_byte(speed >> 8 * (i - 8)))
    m_data.append(0x55)
    print("moving")
    # m_data_hex = [hex(i) for i in m_data]
    uca.frame_send(m_data)
    
    # print(type(m_data_hex[0]))
    #uca.inject_data_frame(0x40 + mid, m_data_hex)
    #print(uca.extract_data(m_data))
    
def test_degree(mid):
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x40 + mid)
    m_data.append(0x01)
    m_data.append(0xa4)
    m_data.append(0x00)
    m_data.append(0xf4)
    m_data.append(0x01)
    m_data.append(0xa0)
    m_data.append(0x8c)
    m_data.append(0x00)
    m_data.append(0x00)
    m_data.append(0x55)
    uca.frame_send(m_data)
    #com.uca.inject_data_frame(0x40 + mid, ['a4', '00', 'f4', '01', 'a0', '8c', '00', '0x00'])
        
    