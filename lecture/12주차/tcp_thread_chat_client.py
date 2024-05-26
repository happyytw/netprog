from socket import *
import threading

port = 3333
BUFFSIZE = 1024

def recvTask(sock):
    while True:
        data = sock.recv(BUFFSIZE)
        print('<-\n', data.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))
print('Connected to server')

# Start the receive task in a new thread
th = threading.Thread(target=recvTask, args=(sock,))
th.start()

while True:
    msg = input()
    print('->', msg)
    sock.send(msg.encode())
