import requests
from bs4 import BeautifulSoup
import schedule # 일정 시간이나 기간마다 자동으로 돌려주기 위한 모듈
import time # 컴퓨터 동작이 빨라서 슬립을 주기 위해 import한 모듈
import os
    
def auto_save_hour():
    
    import requests
    from bs4 import BeautifulSoup
    import schedule # 일정 시간이나 기간마다 자동으로 돌려주기 위한 모듈
    import time # 컴퓨터 동작이 빨라서 슬립을 주기 위해 import한 모듈
    import os
    
    li=[]
    li2=[]
    
    def get_rank():  
        li=[]
        url="https://www.musinsa.com/ranking/keyword" # 무신사 전체 인기검색어 url
        # url을 통해 가져오기
        request=requests.get(url) 
        html_data=request.text
        soup=BeautifulSoup(html_data,"html.parser")

        for f_text in soup.find_all("li"): # 홈페이지의 li를 모두 찾습니다.
            li.append(f_text.a['title']) # 그 <li>안의 <a title>을 임시 리스트에 넣습니다.
        for i in range(20):
            li2.append(li[i]) # 저장해둔 임시 리스트에서 20개만을 다른 리스트에 저장합니다.
        print(li2) # schedule을 돌릴 때 잘 돌아가는지 확인을 위해 출력을 포함합니다.
    
    schedule.every(1).hour.do(get_rank) # 1시간마다 정의해 둔 get_rank 함수를 실행
    while(True): # 무한 반복
        schedule.run_pending() # 스케줄 작동
        time.sleep(1) # 초같은 경우 시스템이 너무 빠를 수 있어서 1초의 슬립을 주었습니다.       
        if(len(li2)==160): # 10시/11시/12시/1시/2시/3시/4시/5시 20*8 길이의 데이터가 되었을때 반복 종료
            break
    return li2

def savefile(lis):
    if(os.path.isfile('save_data.txt')):
        f=open('save_data.txt','a',encoding='utf-8')
        for i in lis:
            f.write(i+'\n')
    else:
        f=open('save_data.txt','w',encoding='utf-8')
        for i in lis:
            f.write(i+'\n')
    f.close()