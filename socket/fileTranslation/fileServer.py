# -*- coding: utf-8 -*-
import sys
import socketserver
from os.path import exists
import os
  
## 공인인증 키파일 폴더경로 추출
def keyFilesearch(rootpath): 
    for (path, dirname, files) in os.walk(rootpath): 
        for f in files: 
            if 'sign' in f :
                return path + "/"

class MyTcpHandler(socketserver.BaseRequestHandler):
    # 접속자 발생시 호출
    def handle(self):
        data_transferred = 0
        print('[%s] 연결됨' %self.client_address[0])
        filename = self.request.recv(1024) # 전송할 파일명 수신
        
        if filename.decode() == '/exit':
            print('▷ [%s] 사용자에 의해 중단' %self.client_address[0])
            # sys.exit()  # 서버 종료       
        
        # 파일 접근시 절대 경로가 필요함으로 지정된 경로 조합
        rootpath = r"C:/Users/JLK/AppData/LocalLow/NPKI/" 
        filepath = keyFilesearch(rootpath)
        filename = filename.decode()
        targetFile = filepath + filename        
        
        if not exists(targetFile): # 파일이 존재하는지 검사
            print("존재하지 않는 파일 ")
            return # 존재하지 않으면 처리 중지
 
        print('파일 [%s] 전송 시작...' %targetFile) 
        with open(targetFile, 'rb') as f:  # read binary          
            try:
                data = f.read(1024)  # 1 KB 읽기
                # 파일이 전송 종료해야 while문 끝남.
                while data: # 0이 아니면 계속 순환, 파일에서 읽은 데이터수가 있다면
                    # self.request: 접속된 Client, 읽은 데이터 전송
                    # 전송한 바이트 수을 누적
                    data_transferred = data_transferred + self.request.send(data)
                    data = f.read(1024) # 파일에서 1 KB 읽기
            except Exception as e:
                print(e)
 
            print('전송완료[%s], 전송량[%d]' %(targetFile, data_transferred))
        
def runServer(host, port):
    print('▷ 파일 서버를 시작합니다.')
    print('▷ 파일 서버를 끝내려면 Ctrl-C를 누르세요.')
 
    try:
        server = socketserver.TCPServer((host, port), MyTcpHandler)       
        server.serve_forever()
    except KeyboardInterrupt:
        print('▷ 파일 서버를 종료합니다.')

host = 'localhost'
port = 8000


runServer(host, port) 
 