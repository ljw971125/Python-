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
'''
함수 : 파스칼 표기법(Pascal case) : 카멜표기법과 같지만 가장 첫 글자 대문자
변수 : 스네이크 표기법(Snake case) : 소문자만 사용, 각 단어 사이에 언더바(_)를 넣는다.
'''
'''
in_num      메뉴
 1         데이터 축적(1시간 마다)
 2         (21~23일간 8시간*3일=24시간(480개))의 최대 빈도수
 3         (21~23일간 8시간*3일=24시간(480개))의 검색어/빈도수의 워드클라우드
 4         (21~23일간 8시간*3일=24시간(480개))의 검색어/빈도수의 막대 그래프
 5         메뉴 2번에서 불러온 검색어와 일치하는 상품의 브랜드 1~10page(900개) 의 브랜드/빈도수 워드클라우드
 6         메뉴 2번에서 불러온 검색어와 일치하는 상품의 브랜드 1~10page(900개) 의 브랜드/빈도수 원 그래프
 0         프로그램 종료
'''


'''
 함수명: ToKorean
            변수명    자료형    설명
매개변수 : 없음
반환값 : 없음
기능설명: 한글 깨짐 해결
'''    

def toKorean(): # 한글 함수
    if platform.system() == 'Darwin': # 맥
        plt.rc('font', family='AppleGothic') 
    elif platform.system() == 'Windows': # 윈도우
        plt.rc('font', family='Malgun Gothic') 
    elif platform.system() == 'Linux': # 리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 
    plt.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

'''
 함수명: createFolder
            변수명    자료형    설명
매개변수 : 없음
반환값 : 없음
기능설명: imsiTemp 폴더 생성
'''             
def createFolder(): # 폴더 생성
    try:
        if not os.path.exists('imsiTemp'): # 폴더이름:imsiTemp의 존재여부 : x
            os.makedirs('imsiTemp') # 'imsiTemp'디렉토리 생성
    except OSError: # os에러
        print ('Error: Creating directory. ' +  'imsiTemp') # os에러일때 화면에 이 문자열을 출력합니다.

'''
함수명: deleteImg
            변수명   자료형    설명
매개변수 : in_num    int       메뉴 번호 (코드라인 11~20 참조)
    값   :  4        int       imsiTemp 폴더안의 stick.jpg 이미지 삭제
    값   :  6        int       imsiTemp 폴더안의 circle.jpg 이미지 삭제
    값   :  3 or 5   int       imsiTemp 폴더안의 wordcloud.jpg 이미지 삭제
              
반환값 : 없음
기능설명   :    생성된 이미지파일 삭제
 '''   

#이미지 삭제
def deleteImg(in_num):
    if(in_num==4):
        os.remove("imsiTemp\\stick.jpg")
    elif(in_num==6):
        os.remove('imsiTemp\\circle.jpg')
    elif(in_num==3 or in_num==5):
        os.remove('imsiTemp\\wordcloud.jpg')
    else:
        print("메인을 수정하세요 매개변수가 잘못받아졌습니다.")

        
'''
함수명: deleteFolder
매개변수 : 없음
반환값 : 없음
기능설명: imsiTemp 폴더 삭제
'''  


def deleteFolder(): # 폴더삭제
    try:
        if os.path.exists('imsiTemp'): # 'imsiTemp' 디렉토리가 존재하면
            shutil.rmtree('imsiTemp') # 전체삭제(파일,폴더 전부다)
    except OSError:
        print ('Error: Creating directory. ' +  'imsiTemp')

'''
 함수명: fileToCounter
            변수명                  자료형          설명
매개변수 : 없음
변수    :   file_list               list           파일에서 데이터를 읽어 저장할 리스트
변수    :   fix_list                list           file_list에서 20개를 추출 해서 저장할 리스트
반환값 :   keyword_list_couter       Counter     정제한 리스트 Counter화
기능설명: 파일에서 데이터를 읽어와 Counter로 반환함
'''    
def fileToCounter():  
    f=open('save_data.txt','r',encoding='utf-8') # 축적된 파일 열기
    file_list=[] # 파일데이터를 읽어서 저장할 임시 리스트
    file_list.append(f.read()) # 임시 리스트에 데이터를 읽어서 저장
    f.close() # 파일닫기
    
    fix_file=[] # file_list에서 20개만을 정제해서 저장할 리스트
    for i in file_list: # 파일에서 읽어서 저장한 리스트를 읽기
        fix_file.append(i.split('\n')) # \n 을 구분으로 임시 저장용 리스트에 저장
    file_list.clear() # 리스트 클리어
    for i in fix_file[0]: # 위의 split으로 2차원 배열이 되었음
        file_list.append(i) # 비워둔 리스트에 붙이기
    file_list=list(filter(len,file_list))  # 빈 공백문자열을 filter로 제거
    
    keyword_list_counter=Counter(file_list) # 리스트를 카운트화
    return keyword_list_counter

'''
함수명: searchTop
            변수명              자료형      설명
매개변수 :  fileToCounter       counter     fileToCounter함수에서 반환받은 Counter
반환값 :    없음
변수   :    str_list            list        받아온 fileToCounter에서 key값들을 list로 변환
변수   :    int_list            list        받아온 fileToCounter에서 value값들을 list로 변환
변수   :    list_to_dict        dict        str_list, int_list로 딕셔너리로 변환
변수   :    sorted_by_value     dict        list_to_dict의 value값을 기준으로 내림차순 정렬
기능설명: 빈도수 상위 20개의 검색어 출력
'''    

# 3일간 최대 많이 나온 검색어 상위 20
def searchTop(fileToCounter):
    str_list=list(fileToCounter.keys()) # 읽어온 카운터의 키값(상품명)을 리스트로 저장
    int_list=list(fileToCounter.values()) # 읽어온 카운터의 value값(빈도수)를 리스트로 저장

    list_to_dict = { x:y for x,y in zip(str_list,int_list) } # 두 개의 리스트를 딕셔너리화 (중복제거 x)
    sorted_by_value = sorted(list_to_dict.items(), key=operator.itemgetter(1), reverse=True) # value(빈도수)값으로 내림차순 정렬
    for i in range(0,20,2): # 한 행당 0~1 / 2~3 / 4~5 .../ 18~19 
        print("%10s \t %10s"%(sorted_by_value[i][0],sorted_by_value[i+1][0])) # 출력

'''
함수명: showBar
            변수명              자료형      설명
매개변수 :  fileToCounter       counter     fileToCounter함수에서 반환받은 Counter
반환값 :    없음
변수   :    str_list            list        받아온 fileToCounter에서 key값들을 list로 변환
변수   :    int_list            list        받아온 fileToCounter에서 value값들을 list로 변환

기능설명: 읽어온 파일을 imsiTemp폴더안에 이미지 저장 후 폴더안에 막대 그래프 이미지로 보여줌
''' 
# 저장된 파일을 바탕으로 막대그래프
def showBar(fileToCounter): #카운터 딕셔너리를 매개변수로 받습니다.

    str_list=list(fileToCounter.keys()) # labels라는 이름의 리스트에 카운터딕셔너리의 keys값을 넣습니다.
    int_list=list(fileToCounter.values()) # values라는 이름의 리스트에 카운터딕셔너리의 values값을 넣습니다.
    fig=plt.figure(figsize=(20,10)) # 이미지 크기
    plt.title("3일간의 검색 빈도수") # 이미지 타이틀
    plt.xlabel("검색어") # 이미지 x축 이름
    plt.ylabel("빈도수") # 이미지 y축 이름
    plt.bar(str_list[:20],int_list[:20],color=['r','g','b','purple','y']) # 20개를 [빨 초 파 보 노]색깔의 순서대로 보여줍니다.
    plt.savefig('imsiTemp\\stick.jpg') # imsiTemp폴더안에 막대.jpg라는 이름의 이미지파일을 저장합니다.
    plt.close(fig) # 이미지를 보여주지 않고 닫습니다.
    for i in range(20):
        print("%s : %d"%(str_list[i],int_list[i]))
    image = Image.open("imsiTemp\\stick.jpg") # 이미지를 불러옵니다.
    image.show() # 불러온 이미지를 보여줍니다.

'''
함수명: searchBrand
            변수명              자료형      설명
매개변수 :  없음
반환값1:    brand_counter       Counter     웹 크롤링해서 가져온 브랜드 리스트를 Counter로 변환 후 반환
반환값2:    1                   int         입력을 중지할 시 임의의 리턴값 반환
변수   :    str_list            list        받아온 fileToCounter에서 key값들을 list로 변환
변수   :    int_list            list        받아온 fileToCounter에서 value값들을 list로 변환
변수   :    list_to_dict        dict        str_list, int_list로 딕셔너리로 변환
변수   :    sorted_by_value     dict        list_to_dict의 value값을 기준으로 내림차순 정렬
변수   :    sorted_list         list        value값으로 정렬된 딕셔너리의 key값 20개 리스트에 저장
변수   :    input_product       str         상품 검색
변수   :    data_url            str         상품 검색 후 url
변수   :    brand_name          str         상품 브랜드이름
변수   :    brand_li            list        상품 브랜드리스트
변수   :    brand_counter       counter     상품에 대한 브랜드 빈도수
기능설명: 무신사 웹 크롤링으로 상품 검색 후 판매순 1년기준 상위제품 900개 브랜드를 읽어와서 Counter반환
'''
# 키워드별 판매순으로 브랜드 카운팅
# 상품 검색후 브랜드 카운팅
def searchBrand():
     # 상품명 입력
    file_to_counter=fileToCounter()
    str_list=list(file_to_counter.keys()) # 읽어온 카운터의 키값(상품명)을 리스트로 저장
    int_list=list(file_to_counter.values()) # 읽어온 카운터의 value값(빈도수)를 리스트로 저장
    list_to_dict = { x:y for x,y in zip(str_list,int_list) } # 두 개의 리스트를 딕셔너리화 (중복제거 x)
    sorted_by_value = sorted(list_to_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_list=[] # 빈리스트
    for i in range(0,20):
        sorted_list.append(sorted_by_value[i][0])

    while(True):
        input_product = input('상품명을 입력해주세요{메뉴화면 돌아가기:y}.')
        if  input_product in sorted_list:
            driver=webdriver.Chrome("C:\chromedriver\chromedriver.exe") #크롬드라이버
            driver.get("https://www.musinsa.com/app/") # 무신사 홈페이지

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
            data_url=URL.split('page')

            brand_li=[] #브랜드 리스트
            for i in range(1,11): # 첫페이지 부터 10페이지 까지 수집
                url = Request(data_url[0]+'page='+str(i)+data_url[1][2:], headers={'User-Agent': 'Mozilla/5.0'})
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


'''
함수명: brandCircle
            변수명              자료형      설명
매개변수 :  없음
반환값 :    없음
변수   :    brand_counter       Counter
변수   :    bc_keys             list
변수   :    bc_values           list
변수   :    high_values         list
변수   :    high_keys           list
변수   :    explode_max         int
변수   :    explode_value       list
기능설명: imsiTemp폴더 안에 원 그래프 이미지 저장 후 불러오기
''' 
# 브랜드 파일 원그래프
def brandCircle():
  
    brand_counter = searchBrand()

    bc_keys=list(brand_counter.keys())
    bc_values=list(brand_counter.values())

    high_values = []
    high_keys=[]
        
    for i in range(len(bc_keys)):
        if(bc_values[i] >= 20):
            high_values.append(bc_values[i])
            high_keys.append(bc_keys[i])
        
    explode_max = 0
    explode_value = []

    for i in range(len(high_values)):
        if high_values[i] > explode_max:
            explode_max = high_values[i]
        
    for i in range(len(high_values)):
        if high_values[i] == explode_max:
            explode_value.append(0.1)
        else:
            explode_value.append(0)
        
      
    plt.pie(high_values, labels=high_keys, explode=explode_value, autopct='%.2f')
    plt.savefig('imsiTemp\\circle.jpg')
    plt.close()
    for i in range(0,len(high_keys)):
        print("%s : %d"%(high_keys[i],high_values[i]))
    image = Image.open("imsiTemp\\circle.jpg")
    image.show()

'''
함수명: mkWordCloud
            변수명             자료형      설명
매개변수 :  func_counter       Counter     Counter값을 반환받는 함수를 매개변수로 받음
반환값 :    없음
변수   :    fc_keys            list        받아온 함수의 counter에서 key값들을 list로 변환
변수   :    fc_values          list        받아온 함수의 counter에서 value값들을 list로 변환
변수   :    wordcloud_dict     dict        fc_keys와 fc_values의 값으로 딕셔너리화
변수   :    t_mask
변수   :    wordcloud_img     이미지오픈  이미지를 열기 위한 변수         
기능설명:   imsiTemp폴더 안에 이미지 저장 후 이미지 불러오기
''' 

# 3일간 검색어 순위 워드 클라우드, 상품 검색 후 브랜드 워드클라우드
def mkWordCloud(func_counter):

    if (func_counter==1):
        print('메뉴화면 이동')
    else:
        fc_keys=list(func_counter.keys())
        fc_values=list(func_counter.values())

        wordcloud_dict = dict(zip(fc_keys,fc_values))
        t_mask = np.array(Image.open('t5_2.jpg'))

        fontpath='C:\\Windows\\Fonts\\NGULIM.TTF'

        wc = WordCloud(
            background_color='white',
            relative_scaling=0.2, 
            mask=t_mask, stopwords=['counter'], 
            colormap ="Greens",
            font_path = fontpath

        ).generate(str(wordcloud_dict))
        plt.figure(figsize=(8,8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.savefig('imsiTemp\\wordcloud.jpg')
        plt.close()
        for i in range(0,len(wordcloud_dict)):
            print("%s : %d"%(fc_keys[i],fc_values[i]))
        wordcloud_img=Image.open('imsiTemp\\wordcloud.jpg')
        wordcloud_img.show()
