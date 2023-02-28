

import requests
from bs4 import BeautifulSoup
import schedule # 일정 시간이나 기간마다 자동으로 돌려주기 위한 모듈
import time # 컴퓨터 동작이 빨라서 슬립을 주기 위해 import한 모듈
import os # 경로상의 파일 존재여부를 확인하기 위해 import한 모듈

# 1시간 마다 자동으로 20개씩 리스트에 저장 후 스케줄이 끝날때 텍스트 파일에 써주는 모듈
def autoSaveHour():
    
    # 파일 저장 모듈
    def saveFile():
        #if(os.path.isfile('rankdata\\save_data.txt')): # 경로상에 save_data.txt 이름의 파일이 있을 경우
        if(os.path.isfile('rankdata\\save_data2.txt')): # 경로상에 save_data2.txt 이름의 파일이 있을 경우
            #f=open('rankdata\\save_data.txt','a',encoding='utf-8') # 파일 append 방식으로 열기
            f=open('rankdata\\save_data2.txt','a',encoding='utf-8')
            for i in fixed_list: # 리스트 값 가져오기
                f.write(i+'\n') # '\n' 으로 줄을 띄우면서 파일에 씁니다
        #else: # 경로상에 save_data.txt 이름의 파일이 없을 경우
            #f=open('rankdata\\save_data.txt','w',encoding='utf-8') # 파일 write 방식으로 열기(write방식으로 없을 경우 자동 생성)
        else:
            f=open('rankdata\\save_data2.txt','w',encoding='utf-8')
            for i in fixed_list: 
                f.write(i+'\n') # '\n' 으로 줄을 띄우면서 파일에 씁니다
        f.close() # 파일 닫기
        
    def getRank():  # 인기 검색어 상위 20개씩 뽑기 위한 함수
        original_list.clear() # 정제하기 전 가져올 리스트 초기화
        url="https://www.musinsa.com/ranking/keyword" # 무신사 전체 인기검색어 url
        # url을 통해 가져오기
        request=requests.get(url) 
        html_data=request.text
        soup=BeautifulSoup(html_data,"html.parser")

        for f_text in soup.find_all("li"): # 홈페이지의 li를 모두 찾습니다.
            original_list.append(f_text.a['title']) # 그 <li>안의 <a title>을 임시 리스트에 넣습니다.
        for i in range(20):
            fixed_list.append(original_list[i]) # 모두 읽어온 original_list에서 20개만을 fixed_list 리스트에 붙여서 값을 넣어줍니다.
        print(fixed_list) # schedule을 돌릴 때 잘 돌아가는지 확인을 위해 출력을 포함합니다.

    original_list=[] # 정제되지 않고 인기 검색어 상위 100개의 데이터를 가져올 리스트
    fixed_list=[] # 상위 100개의 데이터를 20개로 정제해서 데이터를 쌓을 리스트
    
    url="https://www.musinsa.com/ranking/keyword" # 무신사 전체 인기검색어 url
        # url을 통해 가져오기
    request=requests.get(url) 
    html_data=request.text
    soup=BeautifulSoup(html_data,"html.parser")

    for f_text in soup.find_all("li"): # 홈페이지의 li를 모두 찾습니다.
        original_list.append(f_text.a['title']) # 그 <li>안의 <a title>을 임시 리스트에 넣습니다.
    for i in range(20):
        fixed_list.append(original_list[i]) # 저장해둔 임시 리스트에서 20개만을 다른 리스트에 저장합니다.
    print(fixed_list) # schedule을 돌릴 때 잘 돌아가는지 확인을 위해 출력을 포함합니다.
    
    #schedule.every(1).hour.do(get_rank) # 1시간마다 정의해 둔 get_rank 함수를 실행
    schedule.every(5).seconds.do(getRank)
    while(True): # 무한 반복
        schedule.run_pending() # 스케줄 작동
        time.sleep(1) # 초같은 경우 시스템이 너무 빠를 수 있어서 1초의 슬립을 주었습니다.
        #if(len(fixed_list)==160): # 정제된 데이터의 길이가 160 즉, 8시간이 되었을 때(10시부터 실행하여 10시,11시,12시,1시,2시,3시,4시,5시)
        if(len(fixed_list)==60):
            saveFile() # 파일에 저장
            break # 무한 반복 종료