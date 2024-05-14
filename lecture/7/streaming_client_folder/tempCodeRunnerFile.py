import socket
import cv2
import numpy as np

BUF_SIZE = 999999999
LENGTH = 1000000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5001))

while True:
    sock.send(b'start')
    rx_size = 0
    data = b''
    
    while rx_size < LENGTH:  # 이미지 크기 수신
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break
        data = data + rx_buf
        rx_size += len(rx_buf)
        if rx_size < LENGTH:
            break
    
    frame_len = float(data.decode())  # 바이트를 문자열로 디코딩하여 이미지 크기 획득
    sock.send(b'image')
    rx_size = 0
    byteData = b''
    
    while rx_size < frame_len:  # 실제 이미지 수신
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break
        byteData = byteData + rx_buf
        rx_size += len(rx_buf)
        if rx_size < frame_len:
            break
    
    data = np.frombuffer(byteData, dtype='uint8')
    imgDecode = cv2.imdecode(data, 1)
    cv2.imshow('image', imgDecode)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
