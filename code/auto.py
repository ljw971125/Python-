import requests
from bs4 import BeautifulSoup
import schedule # 일정 시간이나 기간마다 자동으로 돌려주기 위한 모듈
import time # 컴퓨터 동작이 빨라서 슬립을 주기 위해 import한 모듈
import os # 경로상의 파일 존재여부를 확인하기 위해 import한 모듈
import sys # 시스템 종료를 위한 import 모듈
import datetime as dt # 오늘 날짜와 시간을 출력하기 위해 import한 모듈


'''
전체 설명 : 1시간마다 자동으로 rankdata 안에 save_data.txt에 자동으로 저장하는 메서드

참고 ) 지금은 5초마다 1번씩 정해진 시간까지 돌아가는 상황입니다. ( 정해진 시간은 줄 번호 : 117 번의 괄호 ( )안에 시간을 정해주시면 됩니다. 표기법은 00:00~24:00 이런식입니다.)
1시간씩 실행할 때
줄 번호 : 113 번을 주석 해제하세요.  그리고  줄 번호 : 115 번을 주석처리 해주세요.
'''
year=dt.datetime.now().year
month=dt.datetime.now().month
day=dt.datetime.now().day

file_name="%04d%02d%02d_축적데이터"%(year,month,day)
'''
 함수명: saveFile
            변수명      자료형    설명
매개변수 :  fixed_list  list      정제된 리스트를 받아온다
반환값 : 없음
기능설명: 매개변수로 받아온 리스트를 .txt파일에 쓰기
'''          
# 파일 저장 모듈
def saveFile(fixed_list):

    if(os.path.isfile('rankdata\\'+file_name)): # 경로상에 save_data2.txt 이름의 파일이 있을 경우
        f=open('rankdata\\'+file_name,'a',encoding='utf-8')
        for i in fixed_list: # 리스트 값 가져오기
            f.write(i+'\n') # '\n' 으로 줄을 띄우면서 파일에 씁니다
    else:
        f=open('rankdata\\'+file_name,'w',encoding='utf-8')
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
    date=dt.datetime.now()
    print("%d년 %d월 %d일 %d시 %d분 %d초 : %s"%(date.year,date.month,date.day,date.hour,date.minute,date.second,fixed_list)) # 돌아가는 것을 보기 위한 출력
    saveFile(fixed_list)  # txt 파일에 저장   

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
    # 스케줄 같은 경우 지정한 시간부터 실행되기 때문에 실행하자마자 1번은 돌립니다.
    try:
        # 실행하자마자 1번은 바로 실행
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
        date=dt.datetime.now() # 현재 년월일시분초 를 보기 위함
        print("%d년 %d월 %d일 %d시 %d분 %d초 : %s"%(date.year,date.month,date.day,date.hour,date.minute,date.second,fixed_list)) # 돌아가는 것을 보기 위한 출력
        saveFile(fixed_list)
        
        # 스케줄
        schedule.every(1).hour.do(getRank) # 1시간마다 정의해 둔 get_rank 함수를 실행    
        # 시험용
        #schedule.every(5).seconds.do(getRank)
        schedule.every().day.at("10:33").do(exit)
        while(True): # 무한 반복
            schedule.run_pending()
            time.sleep(1) # 초같은 경우 시스템이 너무 빠를 수 있어서 1초의 슬립을 주었습니다.


    except SystemExit:
        print("자동 수집을 종료합니다.")
        
