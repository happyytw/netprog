import socket
import threading

# 클라이언트 메시지를 처리하는 함수
def handler(sock):
    while True:
        # 서버로부터 메시지 수신
        msg, addr = sock.recvfrom(1024)
        print(msg.decode())

# 서버 주소 설정
svr_addr = ('localhost', 2500)

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 사용자로부터 ID 입력 받기
my_id = input('ID를 입력하세요: ')

# 사용자 ID를 서버로 전송
sock.sendto(('[' + my_id + ']').encode(), svr_addr)

# 메시지 처리를 담당할 스레드 시작
th = threading.Thread(target=handler, args=(sock,))
th.daemon = True  # 메인 스레드 종료 시 함께 종료되도록 설정
th.start()

# 사용자로부터 메시지 입력받고 서버로 전송
while True:
    msg = '[' + my_id + '] ' + input()
    sock.sendto(msg.encode(), svr_addr)
