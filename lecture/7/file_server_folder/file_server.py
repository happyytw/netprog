from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7778))
sock.listen(10)
print('File server is running...') # 클라이언트에 무슨 파일들이 존재하는지 보내는 것을 추가할 것이다

while True:
    conn, addr = sock.accept()
    
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Hello':  # 압축하기 시험 문제
        print('client:', addr, msg.decode())
        conn.close()
        continue
    else:
        print('client:' ,addr, msg.decode())
    # 'Filename' 메시지 전송
    conn.send(b'Filename')
    # 파일 이름 수신
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    filename = msg.decode()
    print('client:', addr, filename)
    
    try:
        filesize = os.path.getsize(filename)
    except:
        conn.send(b'Nofile')
        conn.close()
        continue
    else:
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)
    
    f = open(filename, 'rb') # read binary
    data = f.read()
    conn.sendall(data)
    
    msg = conn.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print('client:', addr, msg.decode())
        
    f.close()
    conn.close()