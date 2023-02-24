# 기능
#!/usr/bin/env python
# coding: utf-8

#%%
from collections import Counter # 자료형(list, tuple, dict)들에게 확장된 기능을 주기 위해 제작된 파이썬의 내장 모듈
import requests # 특정 웹사이트에 HTTP 요청을 보내 HTML 문서를 받아올 수 있는 라이브러리
from bs4 import BeautifulSoup # 파이썬에서 사용할 수 있는 웹데이터 크롤링 라이브러리
from selenium import webdriver # HTML 값들을 처리함에 있어 동적으로 변하는 웹 페이지의 데이터들까지 크롤링
from selenium.webdriver.common.by import By 
from time import sleep # sleep함수
from urllib.request import urlopen,Request # URL(Uniform Resource Locator)을 가져오기 위한 파이썬 모듈
import matplotlib.pyplot as plt # 데이터를 차트나 플롯(Plot)으로 그려주는 라이브러리 패키지
import platform # 시스템 정보를 확인할 때 사용하는 모듈
from wordcloud import WordCloud # 중요한 단어나 키워드를 시각화해서 보여주는 시각화 도구
import numpy as np # NumPy(Numerical Python)는 파이썬의 고성능 수치계산을 위한 라이브러리
from PIL import Image # 이미지를 분석하고 처리하는 라이브러리
import operator # 파이썬에서 수행 가능한 연산을 효율적으로 처리할 수 있는 모듈
import os # os(Operating System) 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해주는 모듈
import shutil # 폴더 안에 파일이 존재해서 삭제가 안되기 때문에 상관없이 삭제하기 위한 모듈
#%%
def hangul(): # 한글 깨짐 해결
    if platform.system() == 'Darwin': # 맥
        plt.rc('font', family='AppleGothic') 
    elif platform.system() == 'Windows': # 윈도우
        plt.rc('font', family='Malgun Gothic') 
    elif platform.system() == 'Linux': # 리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 
    plt.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

def createFolder(): # 폴더 생성
    try:
        if not os.path.exists('imsiTemp'): # 폴더이름:imsiTemp의 존재여부 : x
            os.makedirs('imsiTemp') # 'imsiTemp'디렉토리 생성
    except OSError: # os에러
        print ('Error: Creating directory. ' +  'imsiTemp') # os에러일때 화면에 이 문자열을 출력합니다.
    
def save_img(num):     # 이미지 저장   
    if(num==1):
        image = Image.open("imsiTemp\\막대.jpg") # imsiTemp폴더 안의 이미지를 열어서 image변수에 저장
        image.save("막대.jpg",'JPEG') # image변수를 현재경로의 매개변수 값으로 저장
    elif(num==2):
        image = Image.open("imsiTemp\\워드클라우드1.jpg")# imsiTemp폴더 안의 이미지를 열어서 image변수에 저장
        image.save("워드클라우드1.jpg",'JPEG') # image변수를 현재경로의 매개변수 값으로 저장
    elif(num==3):
        image = Image.open("imsiTemp\\원그래프.jpg")# imsiTemp폴더 안의 이미지를 열어서 image변수에 저장
        image.save("원그래프.jpg",'JPEG') # image변수를 현재경로의 매개변수 값으로 저장
    else :
        image = Image.open("imsiTemp\\워드클라우드2.jpg")# imsiTemp폴더 안의 이미지를 열어서 image변수에 저장
        image.save("워드클라우드2.jpg",'JPEG') # image변수를 현재경로의 매개변수 값으로 저장
def deleteFolder(): # 폴더삭제
    try:
        if os.path.exists('imsiTemp'): # 'imsiTemp' 디렉토리가 존재하면
            shutil.rmtree('imsiTemp') # 전체삭제(파일,폴더 전부다)
    except OSError:
        print ('Error: Creating directory. ' +  'imsiTemp')

def file_to_counter():  
    f=open('save_data.txt','r',encoding='utf-8') # 축적된 파일 열기
    lis=[] # 데이터를 읽어서 저장할 임시 리스트
    lis.append(f.read()) # 임시 리스트에 데이터를 읽어서 저장
    f.close() # 파일닫기
    
    lis2=[] # 임시 저장용 리스트
    for i in lis: # 파일에서 읽어서 저장한 리스트를 읽기
        lis2.append(i.split('\n')) # \n 을 구분으로 임시 저장용 리스트에 저장
    lis.clear() # 리스트 클리어
    for i in lis2[0]: # 위의 split으로 2차원 배열이 되었음
        lis.append(i) # 비워둔 리스트에 붙이기
    lis=list(filter(len,lis))  # 빈 공백문자열을 filter로 제거
    
    cnt=Counter(lis) # 리스트를 카운트화
    return cnt
       
# 검색어 순위 데이터 20등 까지 보여주는 함수
def get_ranklist():
    # 모듈 불러오기
    
    # 임시 리스트 생성
    li=[]
    li2=[]

    # url을 통한 웹 크롤링
    url="https://www.musinsa.com/ranking/keyword"
    request=requests.get(url)
    html_data=request.text
    soup=BeautifulSoup(html_data,"html.parser")
    
    # 20등 까지의 검색어 순위 리스트 생성
    for f_text in soup.find_all("li"): # <li> 를 모두 찾습니다.
        li.append(f_text.a['title']) # 그 안의 <a title=?>을 찾아서 임시 리스트1에 넣어줍니다.
    for i in range(20): # 20번 반복합니다.
        li2.append(li[i]) # 빈 리스트(li2)안에 li[0~19]까지 넣습니다.
    return li2 # 리스트를 리턴값으로 줍니다.

# 3일간 최대 많이 나온 검색어 상위 20
def search_top(cnt):
    string_list=list(cnt.keys()) # 읽어온 카운터의 키값(상품명)을 리스트로 저장
    int_list=list(cnt.values()) # 읽어온 카운터의 value값(빈도수)를 리스트로 저장

    dic = { x:y for x,y in zip(string_list,int_list) } # 두 개의 리스트를 딕셔너리화 (중복제거 x)
    sorted_by_value = sorted(dic.items(), key=operator.itemgetter(1), reverse=True) # value(빈도수)값으로 내림차순 정렬
    for i in range(0,20,2): # 한 행당 0~1 / 2~3 / 4~5 .../ 18~19 
        print("%10s \t %10s\n"%(sorted_by_value[i][0],sorted_by_value[i+1][0])) # 출력
    return sorted_by_value


# 저장된 파일을 바탕으로 막대그래프
def show_bar(counter): #카운터 딕셔너리를 매개변수로 받습니다.
    if(os.path.isfile("imsiTemp\\막대.jpg")): # 프로그램실행시 자동으로 생성되는 imsiTemp폴더안에 이미지파일이 존재할 경우
        image = Image.open("imsiTemp\\막대.jpg") # 이미지를 엽니다.
        image.show() # 이미지 보여주기
    else: # imsiTemp폴더안에 이미지파일이 존재하지 않을 경우
        labels=list(counter.keys()) # labels라는 이름의 리스트에 카운터딕셔너리의 keys값을 넣습니다.
        values=list(counter.values()) # values라는 이름의 리스트에 카운터딕셔너리의 values값을 넣습니다.
        fig=plt.figure(figsize=(20,10)) # 이미지 크기
        plt.title("3일간의 검색 빈도수") # 이미지 타이틀
        plt.xlabel("검색어") # 이미지 x축 이름
        plt.ylabel("빈도수") # 이미지 y축 이름
        plt.bar(labels[:20],values[:20],color=['r','g','b','purple','y']) # 20개를 [빨 초 파 보 노]색깔의 순서대로 보여줍니다.
        plt.savefig('imsiTemp\\막대.jpg') # imsiTemp폴더안에 막대.jpg라는 이름의 이미지파일을 저장합니다.
        plt.close(fig) # 이미지를 보여주지 않고 닫습니다.
        image = Image.open("imsiTemp\\막대.jpg") # 이미지를 불러옵니다.
        image.show() # 불러온 이미지를 보여줍니다.

# 키워드별 판매순으로 브랜드 카운팅
# 상품 검색후 브랜드 카운팅
def search_brand():
     # 상품명 입력
    cnt=file_to_counter()
    string_list=list(cnt.keys()) # 읽어온 카운터의 키값(상품명)을 리스트로 저장
    int_list=list(cnt.values()) # 읽어온 카운터의 value값(빈도수)를 리스트로 저장
    dic = { x:y for x,y in zip(string_list,int_list) } # 두 개의 리스트를 딕셔너리화 (중복제거 x)
    sorted_by_value = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    li=[] # 빈리스트
    for i in range(0,20):
        li.append(sorted_by_value[i][0])

    while(True):
        input_product = input('상품명을 입력해주세요{메뉴화면 돌아가기:y}.')
        if  input_product in li:
            driver=webdriver.Chrome("C:\chromedriver\chromedriver.exe") #크롬드라이버
            driver.get("https://www.musinsa.com/app/") 

            # 크롬 드라이버 동작 부분
            driver.find_element(By.XPATH,'//*[@id="search_query"]').click()
            sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="search_query"]').send_keys(input_product)
            sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="search_button"]').click()
            sleep(0.1)
            driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/section/div[3]/div/section[1]/header/a/h2').click()
            sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="goodsList"]/div[1]/a[7]/span').click()
            sleep(0.1)
            driver.find_element(By.XPATH,'//*[@id="layerSorting_sale"]/div/label[5]').click()
            sleep(0.1)

            URL=driver.current_url
            test_Url=URL.split('page')

            brand_li=[] #브랜드 리스트
            for i in range(1,11): # 첫페이지 부터 10페이지 까지 수집
                url = Request(test_Url[0]+'page='+str(i)+test_Url[1][2:], headers={'User-Agent': 'Mozilla/5.0'})
                html = urlopen(url)
                soup = BeautifulSoup(html, 'html.parser')
                brand_name=soup.find_all('p',class_="item_title")

                for j in range(len(brand_name)):
                    brand_li.append(brand_name[j].text)

            brand_counter = Counter(brand_li)
            return brand_counter
        elif (input_product=='y'or input_product=='Y'):
            return 1
        else:
            print('다시 입력해주세요.')



# 브랜드 파일 원그래프
def brand_circle():
    if(os.path.isfile("imsiTemp\\원그래프.jpg")):
        image = Image.open("imsiTemp\\원그래프.jpg")
        image.show()
    else:        
        counter = search_brand()

        labels=list(counter.keys())
        values=list(counter.values())

        high_value = []
        high_label=[]
        
        for i in range(len(labels)):
            if(values[i] >= 20):
                high_value.append(values[i])
                high_label.append(labels[i])
        
        explode_max = 0
        explode_value = []

        for i in range(len(high_value)):
            if high_value[i] > explode_max:
                explode_max = high_value[i]
        
        for i in range(len(high_value)):
            if high_value[i] == explode_max:
                explode_value.append(0.1)
            else:
                explode_value.append(0)
        
      
        plt.pie(high_value, labels=high_label, explode=explode_value, autopct='%.2f')
        plt.savefig('imsiTemp\\원그래프.jpg')
        plt.close()
        image = Image.open("imsiTemp\\원그래프.jpg")
        image.show()

# 3일간 검색어 순위 워드 클라우드, 상품 검색 후 브랜드 워드클라우드
def mk_wordcloud(func,num):
    if(num==1):
        if(os.path.isfile('imsiTemp\\워드클라우드1.jpg')):
            image=Image.open('imsiTemp\\워드클라우드1.jpg')
            image.show()
        else:
            labels=list(func.keys())
            values=list(func.values())
            high_value2 = [] 
            high_label2 = []

            for i in range(len(labels)):
                if(values[i] >= 5):
                    high_value2.append(values[i])
                    high_label2.append(labels[i])

            high_dic = dict(zip(high_label2,high_value2))

            t_mask = np.array(Image.open('t5_2.jpg')) # 워드클라우드 모양

            fontpath='C:\\Windows\\Fonts\\NGULIM.TTF'

            wc = WordCloud(
                background_color='white',
                relative_scaling=0.2, 
                mask=t_mask, stopwords=['counter'], 
                colormap ="Greens",
                font_path = fontpath
            ).generate(str(high_dic))

            fig=plt.figure(figsize=(8,8))
            plt.imshow(wc, interpolation='bilinear')
            plt.axis('off')
            plt.savefig('imsiTemp\\워드클라우드1.jpg')
            plt.close()
            image=Image.open('imsiTemp\\워드클라우드1.jpg')
            image.show()
    elif(num==2):
        if (func==1):
            print('메뉴화면 이동')
        else:
            if(os.path.isfile('imsiTemp\\워드클라우드2.jpg')):
                image=Image.open('imsiTemp\\워드클라우드2.jpg')
                image.show()
            else:
                labels=list(func.keys())
                values=list(func.values())
                high_value2 = [] 
                high_label2 = []

                for i in range(len(labels)):
                    if(values[i] >= 5):
                        high_value2.append(values[i])
                        high_label2.append(labels[i])

                high_dic = dict(zip(high_label2,high_value2))

                t_mask = np.array(Image.open('t5_2.jpg'))

                fontpath='C:\\Windows\\Fonts\\NGULIM.TTF'

                wc = WordCloud(
                    background_color='white',
                    relative_scaling=0.2, 
                    mask=t_mask, stopwords=['counter'], 
                    colormap ="Greens",
                    font_path = fontpath
                ).generate(str(high_dic))

                plt.figure(figsize=(8,8))
                plt.imshow(wc, interpolation='bilinear')
                plt.axis('off')
                plt.savefig('imsiTemp\\워드클라우드2.jpg')
                plt.close()
                image=Image.open('imsiTemp\\워드클라우드2.jpg')
                image.show()
    else:
        print("잘못된 인자값입니다. 1 2 중 선택해주세요.")