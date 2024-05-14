from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('https://medlms.sch.ac.kr/courses/31991/external_tools/1', 80))
sock.send(b'GET / HTTP/1.1\r\r\n')
data = sock.recv(100)
print(data.decode())
sock.close()