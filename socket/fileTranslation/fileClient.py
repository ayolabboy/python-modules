# -*- coding: utf-8 -*-
import sys, socket
import os

def getFileFromServer(host, port, filename):
    data_transferred = 0
    filepath = r"C:/Users/JLK/"                 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port)) # 서버 연결
        sock.sendall(filename.encode()) # 파일명 전송, 서버 종료: /exit
 
        data = sock.recv(1024) # 파일 수신
        if not data: # 읽은 데이터 없는 경우
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' %filename)
            return 

        with open(filepath+filename, 'wb') as f:
            try:
                while data: # 수신된 데이터가 있으면 계속 실행
                    f.write(data) # 1KB 기록
                    data_transferred = data_transferred + len(data) # 수신받은 데이터 산출
                    data = sock.recv(1024) # 새로운 1 KB 데이터 수신
            except Exception as e:
                print(e)

            print('파일 [%s] 전송종료. 전송량 [%d]' %(filename, data_transferred))
            
            # 파일 전송 받으면 네트워크 종료 

while True:  # 무한 루틴
    print('종료는 \'/exit\' 입니다.');
    filename = input('다운로드 받을 파일이름을 입력하세요: ')
 
    if filename == '/exit':
        sys.exit()
        
    host = 'localhost'
    port = 8000
    
    # 접속 시도              
    getFileFromServer(host, port, filename) 
   