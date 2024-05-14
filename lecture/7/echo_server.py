from socket import *
port = 2500
BUFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)
while True:
    data = conn.recv(BUFSIZE)
    print("Received message: ", data.decode())
    conn.send(data)
    
conn.close() #문제가 없는 이상 계속 실행이 될 것을 의미
sock.close() #문제가 없는 이상 계속 실행이 될 것을 의미