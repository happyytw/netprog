from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(10)

while True:
    client_socket, addr = server_socket.accept()

    data = client_socket.recv(1024).decode()
    filename = 'iot.png'

    try:
        with open(filename, 'rb') as f:
            content = f.read()
            mime_type = 'text/html' if filename.endswith('.html') else 'image/png' if filename.endswith('.png') else 'image/x-icon' if filename.endswith('.ico') else None
            if mime_type:
                response = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n".encode() + content
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\n\r\n<html><head><title>Not Found</title></head><body><h1>Not Found</h1></body></html>".encode()

    client_socket.send(response)
    client_socket.close()

server_socket.close()
