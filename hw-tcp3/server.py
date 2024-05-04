from socket import *

# 웹 서버 소켓 열기
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

print("Listening on port 80...")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    # 요청 라인 분석
    if len(req) < 1:
        c.close()
        continue
    
    request_line = req[0]
    request_parts = request_line.split()

    if len(request_parts) < 3:
        c.close()
        continue
    
    filename = request_parts[1][1:]  # 파일 이름 추출 ("/" 제거)

    # 현재 디렉토리 기준으로 파일 경로 설정
    filepath = './' + filename

    print(filename)
    # 해당 파일이 존재하는지 확인하고, MIME 타입 설정
    if filename == "index.html":
        try:
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
            print("성공")
        except FileNotFoundError:
            print("에러")
            # 파일이 없는 경우 404 응답 전송
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            c.sendall(response.encode())
            c.close()
            continue
    elif filename == "iot.png":
        try:
            f = open(filepath, 'rb')
            mimeType = 'image/png'
            
        except FileNotFoundError:
            # 파일이 없는 경우 404 응답 전송
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            c.sendall(response.encode())
            c.close()
            continue
    elif filename == "favicon.ico":
        print(filename)
        try:
            f = open(filepath, 'rb')
            mimeType = 'image/x-icon'
        except FileNotFoundError:
            print("에러2)")
            # 파일이 없는 경우 404 응답 전송
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
            c.sendall(response.encode())
            c.close()
            continue
    else:
        # 지원하지 않는 자원 요청인 경우 404 응답 전송
        response = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.sendall(response.encode())
        c.close()
        continue

    # HTTP 응답 헤더 전송
    response_headers = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
    c.sendall(response_headers.encode())

    # 파일 내용 읽어서 전송
    if 'text' in mimeType:
        data = f.read()
        c.sendall(data.encode('utf-8'))
    else:
        data = f.read()
        c.sendall(data)

    # 소켓 닫기
    c.close()