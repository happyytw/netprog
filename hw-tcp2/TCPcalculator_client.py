from socket import *

# 서버와 연결
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

# 계산식 입력 및 서버로 전송
while True:
    expression = input('Enter a calculation: ')
    if expression.lower() == 'q':
        break
    
    s.send(expression.encode())
    
    # 서버로부터 결과 수신 및 출력
    result = s.recv(1024).decode()
    print('Result:', result)

# 연결 종료
s.close()
