


def silo_recv():
    com.uca.frame_receive() 
    frame_can = com.uca.extract_data(com.uca.frame)
    id = int(frame_can.get('frame_id'), 16)
    data = frame_can['data']
    if id == 8:
        print(data)
        return 