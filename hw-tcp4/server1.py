from socket import *
import sys

BUFF_SIZE = 1024
PORT = 5555

messages = {}

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', PORT))

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    msg = data.decode()
    print('Received:', msg)
    
    if msg.startswith('send '):
        parts = msg.split(' ', 2)
        messagesID, message = parts[1], parts[2]
        if messagesID not in messages:
            messages[messagesID] = []
        messages[messagesID].append(message)
        s_sock.sendto('OK'.encode(), addr)
    
    elif msg.startswith('receive '):
        parts = msg.split(' ')
        messagesID = parts[1]
        if messagesID in messages and messages[messagesID]:
            message = messages[messagesID].pop(0)
            s_sock.sendto(message.encode(), addr)
        else:
            s_sock.sendto('No messages'.encode(), addr)
    
    elif msg == 'quit':
        break

s_sock.close()
sys.exit()