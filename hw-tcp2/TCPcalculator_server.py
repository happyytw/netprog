from socket import *

# 서버 소켓 생성
server_socket = socket(AF_INET, SOCK_STREAM)

# 포트와 호스트 지정
server_socket.bind(('localhost', 3333))

# 클라이언트의 연결을 기다림
server_socket.listen(1)
print('TCP calculator server is running...')

while True:
    # 클라이언트의 연결 수락
    client_socket, addr = server_socket.accept()
    print('Connected with', addr)
    
    while True:
        # 클라이언트로부터 계산식 받기
        expression = client_socket.recv(1024).decode()
        print('Received expression:', expression)
        
        # 클라이언트 소켓 닫기
        if expression == 'q':
            client_socket.close()
            break
        
        # 계산 실시
        try:
            result = eval(expression)
            result_str = '{:.1f}'.format(result) if isinstance(result, float) else str(result)
        except:
            result_str = 'Invalid expression'
        
        # 결과 클라이언트에게 전송
        client_socket.send(result_str.encode())
        
        

# 서버 소켓 닫기
server_socket.close()
