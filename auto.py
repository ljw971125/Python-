import requests
from bs4 import BeautifulSoup
import schedule # 일정 시간이나 기간마다 자동으로 돌려주기 위한 모듈
import time # 컴퓨터 동작이 빨라서 슬립을 주기 위해 import한 모듈
import os # 경로상의 파일 존재여부를 확인하기 위해 import한 모듈
import sys # 시스템 종료를 위한 import 모듈

'''
전체 설명 : 1시간마다 자동으로 rankdata 안에 save_data.txt에 자동으로 저장하는 메서드

참고 ) 지금은 5초마다 1번씩 정해진 시간까지 돌아가는 상황입니다.
1시간씩 실행할 때
줄 번호 : 27,28,33,34,129 번을 주석 해제하세요.  그리고  줄 번호 : 29,30,35,36,131 번을 주석처리 해주세요.
'''


'''
 함수명: saveFile
            변수명      자료형    설명
매개변수 :  fixed_list  list      정제된 리스트를 받아온다
반환값 : 없음
기능설명: 매개변수로 받아온 리스트를 .txt파일에 쓰기
'''          
# 파일 저장 모듈
def saveFile(fixed_list):

    #if(os.path.isfile('rankdata\\save_data.txt')): # 경로상에 save_data.txt 이름의 파일이 있을 경우
        #f=open('rankdata\\save_data.txt','a',encoding='utf-8') # 파일 append 방식으로 열기    
    if(os.path.isfile('rankdata\\save_data2.txt')): # 경로상에 save_data2.txt 이름의 파일이 있을 경우
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


'''
 함수명: getRank
            변수명      자료형    설명

매개변수 :  original_list  list      정제된 리스트를 받아온다
매개변수 :  fixed_list  list      정제된 리스트를 받아온다
반환값 : 없음
기능설명: 매개변수로 받아온 리스트를 정제한 후 saveFile함수를 불러서 파일에 쓰기
중요사항: 스케줄로 쓰일 함수
'''          
# 스케줄 돌리기위한 메서드
def getRank():  # 인기 검색어 상위 20개씩 뽑기 위한 함수
    
    original_list=[] # 정제하기 전 가져올 리스트 초기화
    fixed_list=[]
    
    url="https://www.musinsa.com/ranking/keyword" # 무신사 전체 인기검색어 url
    # url을 통해 가져오기
    request=requests.get(url) 
    html_data=request.text
    soup=BeautifulSoup(html_data,"html.parser")

    for f_text in soup.find_all("li"): # 홈페이지의 li를 모두 찾습니다.
        original_list.append(f_text.a['title']) # 그 <li>안의 <a title>을 임시 리스트에 넣습니다.
    for i in range(20):
        fixed_list.append(original_list[i]) # 모두 읽어온 original_list에서 20개만을 fixed_list 리스트에 붙여서 값을 넣어줍니다.
    print(fixed_list)   # 돌아가는 것을 보기 위한 출력
    saveFile(fixed_list)  # txt 파일에 저장


'''
 함수명: getRank1
            변수명        자료형    설명

매개변수 :  original_list  list     정제가 되지 않은 리스트를 받아온다
매개변수 :  fixed_list     list     정제된 리스트를 받아온다
반환값 : 없음
기능설명: 매개변수로 받아온 리스트를 정제한 후 saveFile함수를 불러서 파일에 쓰기
중요사항: getRank는 스케줄로 쓰이기 때문에 실행하자마자 찍히지가 않아서 실행시 바로 찍어주는 함수
'''      
# 실행 시점으로 웹 크롤링하는 메서드
def getRank1():  # 인기 검색어 상위 20개씩 뽑기 위한 함수
    
    original_list=[] # 정제하기 전 가져올 리스트 초기화
    fixed_list=[]
    
    url="https://www.musinsa.com/ranking/keyword" # 무신사 전체 인기검색어 url
    # url을 통해 가져오기
    request=requests.get(url) 
    html_data=request.text
    soup=BeautifulSoup(html_data,"html.parser")

    for f_text in soup.find_all("li"): # 홈페이지의 li를 모두 찾습니다.
        original_list.append(f_text.a['title']) # 그 <li>안의 <a title>을 임시 리스트에 넣습니다.
    for i in range(20):
        fixed_list.append(original_list[i]) # 모두 읽어온 original_list에서 20개만을 fixed_list 리스트에 붙여서 값을 넣어줍니다.
    print(fixed_list)  
    saveFile(fixed_list)

 
'''
 함수명:  exit
            변수명      자료형    설명

매개변수 :  없음
반환값 : 없음
기능설명: 스케줄 작동시 강제로 종료시키기 위한 함수
'''      
 # 시스템종료시키는 함수   
def exit():
    sys.exit()

'''
 함수명: autoSaveHour
            변수명      자료형    설명

매개변수 :   없음
반환값 : 없음
기능설명 : 스케줄을 돌려서 정해진 시간까지 1시간마다 txt파일에 저장합니다.
중요사항 : 127번째 줄에 at 뒤에 숫자를 시간으로 변경해 주셔야 정해진 시간까지 자동으로 돌아갑니다.
'''      
# 스케줄 작동 함수    
def autoSaveHour():
    
    try:
        getRank1() # 웹 크롤링하여 바로 파일에 20개 쓰기

        #schedule.every(1).hour.do(getRank) # 1시간마다 정의해 둔 get_rank 함수를 실행    
        # 시험용
        schedule.every(5).seconds.do(getRank)
        schedule.every().day.at("15:52").do(exit)
        while(True): # 무한 반복
            schedule.run_pending() # 스케줄 작동
            time.sleep(1) # 초같은 경우 시스템이 너무 빠를 수 있어서 1초의 슬립을 주었습니다.

    except SystemExit:
        print("자동 수집을 종료합니다. (save_data2.txt에 저장되었습니다.)")
        
