# 기능
#!/usr/bin/env python
# coding: utf-8


from collections import Counter # 자료형(list, tuple, dict)들에게 확장된 기능을 주기 위해 제작된 파이썬의 내장 모듈
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

'''
함수 : 카멜 표기법(Camel case) : 첫문자는 소문자로 사용하며, 단어마다 첫문자를 대문자로 한다.
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

# 저장시의 답변을 리스트로 했습니다.
liYES=['y',"yes","Y","YES","Yes","네","예","넵","옙","ㅔ","ㅇ","ㅇㅋ","그래","그래요","그래용","ㅛ"]
liNO=["n","no","N","NO","No","아니요","x","X","ㄴ","아니","싫어","싫어요","안할래요","안 할래요","ㅜ"]

'''
 함수명: createImsiFolder
            변수명    자료형    설명
매개변수 : 없음
반환값 : 없음
기능설명: imsiTemp 폴더 생성
'''             
def createImsiFolder(): # 폴더 생성
    try:
        if not os.path.exists('imsiTemp'): # 폴더이름:imsiTemp의 존재여부 : x
            os.makedirs('imsiTemp') # 'imsiTemp'디렉토리 생성
    except OSError: # os에러
        print ('Error: Creating directory. ' +  'imsiTemp') # os에러일때 화면에 이 문자열을 출력합니다.

'''
 함수명: createImgFolder
            변수명    자료형    설명
매개변수 : 없음
반환값 : 없음
기능설명: saveImg 폴더 생성
'''             
def createImgFolder(): # 폴더 생성
    try:
        if not os.path.exists('saveImg'): # 폴더이름:imsiTemp의 존재여부 : x
            os.makedirs('saveImg') # 'imsiTemp'디렉토리 생성
    except OSError: # os에러
        print ('Error: Creating directory. ' +  'saveImg') # os에러일때 화면에 이 문자열을 출력합니다.

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
함수명: menu
            변수명    자료형    설명
매개변수 : 없음
반환값 : 없음
기능설명: 메뉴 UI
'''  
def menu():
    print('*'*50)
    print("\t무신사 쇼핑몰의 데이터 수집 및 분석") 
    print('*'*50,'\n')
    print("1) 데이터 크롤링 이후 축적") # bs4
    print("2) 02/21~23(3)일간 최대 많이 나온 검색어 상위 20") 
    print("3) 02/21~23(3)일간 수집한 검색어의 빈도수 워드 클라우드") 
    print("4) 02/21~23(3)일간 검색어 순위 막대 그래프") 
    print("5) 상품 검색 후 브랜드 워드클라우드") #셀레니움
    print("6) 상품 검색 후 브랜드 원 그래프")
    print("0) 종료\n")


'''
함수명: star
            변수명    자료형    설명
매개변수 : 없음
반환값 : 없음
기능설명: 별 50개 찍어주는 함수
'''  
def star():
    print('*'*50)


'''
함수명: subMenuIntro
            변수명    자료형    설명
매개변수 :  in_num    int      메뉴번호
반환값 : 없음
기능설명: 메뉴안에서 메뉴번호를 눌렀을 때 그 메뉴에 대한 설명
'''  
def subMenuIntro(in_num):
    if(in_num==2):
        star()
        print(" 02/21~23(3)일간 최대 많이 나온 검색어 상위 20")
        star()
        print()
    elif(in_num==3):
        star()
        print("\t수집한 검색어의 빈도수 워드 클라우드")
        star()
    elif(in_num==4):
        star()
        print("\t3일간 검색어 순위 막대 그래프")
        star()
    elif(in_num==5):
        star()
        print("\t상품 검색 후 브랜드 워드클라우드")
        star()
        print()
    elif(in_num==6):
        star()
        print("\t수집한 검색어의 빈도수 원 그래프")
        star()
        print()
    elif(in_num==0):
        star()
        print("\t   이용해 주셔서 감사합니다.")
        star()


'''
함수명: doMenu
            변수명      자료형              설명
매개변수 :  in_num      int                 메뉴번호
매개변수 :  func_name   str                 적용할 함수 이름
변수    :   counter     counter / int       함수실행시 반환되는 반환값을 저장할 변수(카운터 딕셔너리 / 1 을 반환받습니다.)

            in_num      func_name           설명
            2           searchTop           빈도수 상위 20개의 검색어
            3           mkWordcloud         카운터 값을 받아서 워드클라우드 생성
            4           showBar             카운터 값을 받아서 막대그래프 생성
            5           mkWordcloud         카운터 값을 받아서 워드클라우드 생성
            6           brandCircle         카운터 값을 받아서 원 그래프 생성
            0           없음('')            임시 폴더 삭제                
반환값 : 없음
기능설명: 메뉴 번호와 함수이름을 입력받아서 함수들을 실행
'''  
def doMenu(in_num,func_name):
    if(in_num==2):
        subMenuIntro(in_num)
        func_name(fileToCounter())  # 빈도수 상위 20개의 검색어
        print()
    elif(in_num==3 or in_num==4):  # 정적인(변하지 않는) 메뉴
        subMenuIntro(in_num)
        func_name(fileToCounter()) 
        answerStaticSave(in_num)
        print()
    elif(in_num==5 or in_num==6): # 동적인(계속 변하는) 메뉴
        subMenuIntro(in_num)
        searchTop(fileToCounter())
        print()
        while(True):
            input_product = input('상품명을 입력해주세요.(메뉴화면 돌아가기:y) : ')
            if(input_product in liYES):
                break    
            else:
                counter=searchBrand(input_product)
                if(counter==1):
                    print("빈도수 상위 20개의 검색어에 포함되지 않았습니다.\n")
                    continue
                else:
                    func_name(counter)
                    answerDynamicSave(in_num)
                    break
        print()
    else:
        deleteimsiFolder()              # imsiTemp폴더(내용있든 없든)삭제              
        subMenuIntro(in_num)

'''
함수명: answerStaticSave
            변수명      자료형      설명
매개변수    in_num      int         메뉴 번호
변수        question    input(str)  저장할지 물어보는 문자열
변수        exist       str         메뉴에서 반복문을 반복하기 위한 반한값
변수        noexist     str         메뉴에서 반복문을 종료하기 위한 반환값
사용함수    saveImg     function    이미지 저장 함수
사용함수    deleteImg   function    imsiTemp안의 이미지 삭제 함수
              
반환값 : 없음
기능설명   :  정적 이미지 저장 질문 후 저장
 '''
def answerStaticSave(in_num):
    question=input("\n이미지를 저장하시겠습니까? (Y/N) : ")
    if(question in liYES):
        print("정적이라 정해진 이름으로 저장합니다.")
        saveImg(in_num,'') # saveImg폴더안에 이미지 저장
        deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
        print()
    elif(question in liNO):
        print("저장하지 않습니다.\n")
        deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
        print()
    else:
        print("잘못 입력하셨습니다.(저장하지 않습니다.\n)")
        deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
        print()

'''
함수명: answerDynamicSave
            변수명      자료형      설명
매개변수    in_num      int         메뉴 번호
변수        question    input(str)  저장할지 물어보는 문자열
변수        img_name    input(str)  저장할 때 입력받을 파일이름 
사용함수    saveImg     function    이미지 저장 함수
사용함수    deleteImg   function    imsiTemp안의 이미지 삭제 함수
              
반환값 : 없음
기능설명   :  동적 이미지 저장 질문 후 임시포 실행
 '''
def answerDynamicSave(in_num):   
    question=input("\n이미지를 저장하시겠습니까? (Y/N) : ")
    if(question in liYES):
        while(True):
            image_name=input("저장하고 싶은 이미지파일명 : ") 
            answer=saveImg(in_num,image_name) # answer변수에 리턴값 받아오기
            if(answer=='rename'): # 받아온 answer변수의 값이 q일때 image_name값 다시 입력
                continue  # 다시 반복
            else: # 받아온 answer변수의 값이 no일때 이미지 저장
                break # 반복 종료
        deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
        print()
    elif(question in liNO):
        print("저장하지 않습니다.\n")
        deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
        print()
    else:
        print("잘못 입력하셨습니다.(저장하지 않습니다.)\n")
        deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
        print()

'''
함수명: saveImg
            변수명              자료형      설명
매개변수    in_num              int         메뉴 번호
매개변수    image_name          str         받아온 이미지 이름 (정적일때는 지정된이름값을 넣어주었습니다.)
변수        imsiImg_name        str         imsiTemp폴더안에 자동 저장될 이미지 이름 메뉴마다 다름
변수        image               imageopen   파일 열기
변수        answer              str         동적인 이미지저장 때의 반환값 저장할 변수
사용함수    staticImgExist      function    
사용함수            
반환값 : 없음
기능설명   :   이미지 저장
 '''
def saveImg(in_num,image_name):     # 이미지 저장
    if(in_num==4):
        imsiImg_name='막대.jpg'
        image_name='막대.jpg'
        staticImgSave(imsiImg_name,image_name)

    elif(in_num==3):
        imsiImg_name='wordcloud.jpg'
        image_name='SF_wordcloud.jpg'
        staticImgSave(imsiImg_name,image_name)

    elif(in_num==6): # 원그래프
        imsiImg_name='circle.jpg'
        answer=dynamicImgSave(imsiImg_name,image_name)
        return answer
    
    elif(in_num==5) : # 워드클라우드
        imsiImg_name='wordcloud.jpg'
        answer=dynamicImgSave(imsiImg_name,image_name)
        return answer
    else:
        print("메인을 수정하세요 매개변수가 잘못되었습니다.\n")

'''
함수명: staticImgSave
            변수명          자료형      설명
매개변수    imsiImg_name      str       받아올 임시폴더의 이미지 이름
매개변수    image_name        str       받아온 이미지 이름
변수        image            imageopen  파일 열기
            
반환값 : 없음
기능설명   :   정적인 이미지(메뉴 3,4번) 이미지 저장
 '''
def staticImgSave(imsiImg_name,image_name):
    if(os.path.isfile(('saveImg\\'+image_name))):
        print("같은 이름의 이미지가 이미 존재합니다.")
    else:
        image = Image.open("imsiTemp\\"+imsiImg_name) # imsiTemp폴더 안의 이미지를 열어서 image변수에 저장
        image.save(("saveImg\\"+image_name),"JPEG")
        
'''
함수명: dynamicImgSave
            변수명          자료형      설명
매개변수    imsiImg_name    str       받아올 임시폴더의 이미지 이름
매개변수    image_name      str       받아온 이미지 이름
변수        image           imageopen  파일 열기
            
반환값 :    rename          str         파일이 존재할 경우 반복을 위해 반환시켜줄 문자열
반환값 :    no_renmae       str         파일이 존재하지 않을 경우 반복문을 탈출하기 위한 반환값

기능설명   :   동적인 이미지(메뉴 5,6번) 이미지 저장
 '''
def dynamicImgSave(imsiImg_name,image_name):
    if(os.path.isfile("saveImg\\"+image_name+".jpg")):
        print("같은 이름의 이미지가 이미 존재합니다.")
        rename='rename'
        return rename
    else:
        image = Image.open(("imsiTemp\\"+imsiImg_name))# imsiTemp폴더 안의 이미지를 열어서 image변수에 저장
        image.save(("saveImg\\"+image_name+".jpg"),"JPEG") # image변수를 현재경로의 매개변수 값으로 저장
        no_rename='no'
        return no_rename

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
    f_name='imsiTemp'
    if(os.path.isdir(f_name)):
        if(in_num==4):
            img_name='막대.jpg'
            removeImgFile(f_name,img_name)
        elif(in_num==6):
            img_name='circle.jpg'
            removeImgFile(f_name,img_name)
        elif(in_num==3 or in_num==5):
            img_name='wordcloud.jpg'
            removeImgFile(f_name,img_name)
        else:
            print("메인을 수정하세요 매개변수가 잘못받아졌습니다.\n")
    else:
        print("폴더가 없습니다.\n")
'''
함수명: removeImgFile
            변수명          자료형          설명
매개변수 : f_name           str             폴더이름
매개변수 : img_name         str             저장할 파일 이름
반환값 : 없음
기능설명 : 이미지 삭제
'''         
def removeImgFile(f_name,img_name):
    if(os.path.isfile((f_name+'\\'+img_name))):
        os.remove((f_name+'\\'+img_name))
    else:
        print(img_name+"가 없습니다.\n")

'''
함수명: deleteimsiFolder
매개변수 : 없음
반환값 : 없음
기능설명: imsiTemp 폴더 삭제
'''  


def deleteimsiFolder(): # 폴더삭제
    try:
        if os.path.exists('imsiTemp'): # 'imsiTemp' 디렉토리가 존재하면
            shutil.rmtree('imsiTemp') # 전체삭제(파일,폴더 전부다)
    except OSError:
        print ('Error: Creating directory. ' +  'imsiTemp\n')

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
    f=open('rankdata\\save_data.txt','r',encoding='utf-8') # 축적된 파일 열기
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
    plt.savefig('imsiTemp\\막대.jpg') # imsiTemp폴더안에 막대.jpg라는 이름의 이미지파일을 저장합니다.
    plt.close(fig) # 이미지를 보여주지 않고 닫습니다.
    print()
    for i in range(20):
        print("%s : %d"%(str_list[i],int_list[i]))
    image = Image.open("imsiTemp\\막대.jpg") # 이미지를 불러옵니다.
    image.show() # 불러온 이미지를 보여줍니다.

'''
함수명: searchBrand
            변수명              자료형      설명
매개변수 :  input_product       str         input으로 입력받아올 문자
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
def searchBrand(input_product):
     # 상품명 입력
    file_to_counter=fileToCounter()
    str_list=list(file_to_counter.keys()) # 읽어온 카운터의 키값(상품명)을 리스트로 저장
    int_list=list(file_to_counter.values()) # 읽어온 카운터의 value값(빈도수)를 리스트로 저장
    list_to_dict = { x:y for x,y in zip(str_list,int_list) } # 두 개의 리스트를 딕셔너리화 (중복제거 x)
    sorted_by_value = sorted(list_to_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_list=[] # 빈리스트
    for i in range(0,20):
        sorted_list.append(sorted_by_value[i][0])

    if  input_product in sorted_list:
        driver=webdriver.Chrome("C:\chromedriver\chromedriver.exe") #크롬드라이버
        driver.get("https://www.musinsa.com/app/") # 무신사

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
    else:
        return 1
            
            

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
def brandCircle(brand_counter):
    if(os.path.isfile("imsiTemp\\circle.jpg")):        #만약 circle.png라는 파일이 있으면
        image = Image.open("imsiTemp\\circle.jpg")     #image 변수에 circle.png파일 대입
        image.show()                                   #image 변수에 저장된 사진 출력
    else:                                              #위 조건이 아니라면
        brand_counter = brand_counter                 #search_brand 메소드에서 크롤링한 데이터를 brand_counter 변수에 대입

        bc_keys=list(brand_counter.keys())             #brand_counter의 key값을 bc_keys 변수에 대입
        bc_value=list(brand_counter.values())          #brand_counter의 value값을 bc_value 변수에 대입

                                                       #↓↓데이터가 너무 많아 value값이 20이상인 데이터만 출력하는 코드↓↓

        high_keys=[]                                   #value값이 20이상인 key값을 대입하는 변수
        high_values = []                               #value값이 20이상인 value값을 대입하는 변수
        del_word_list=['[72시간세일]','[브랜드 위크]','[위클리특가]','[오늘만이가격]','72시간세일','브랜드 위크','위클리특가','오늘만이가격']
        
        for i in range(len(bc_keys)):                  #bc_keys의 길이만큼 반복
            if(bc_value[i] >= 20):                    #만약 bc_value의 i번째 값이 20 이상일 때
                if bc_keys[i] in del_word_list:
                    pass
                else:
                    high_values.append(bc_value[i])
                    high_keys.append(bc_keys[i])
                
                                                       
        value_max = 0                                  #high_values값의 max값 저장 변수
        explode_value = []                             #explode: 원그래프 중심에서 멀어지는 정도, explode값 저장 변수

        for i in range(len(high_values)):              #high_values 길이만큼 반복
            if high_values[i] > value_max:             #만약 high_values의 i번째가 value_max보다 크다면
                value_max = high_values[i]             #value_max 변수에 high_values의 i번째 대입
                                                       #↓↓high_values변수의 길이만큼 explode값 추가하는 코드↓↓
        for i in range(len(high_values)):              #high_values 길이만큼 반복
            if high_values[i] == value_max:            #만약 hige_values의 i번째 값이 value_max값과 같다면
                explode_value.append(0.1)              #explode_value값에 0.1 대입, 0.1값은 중심에서 멀어지는 정도의 값이다.
            else:                                      #조건을 만족하지 못한다면
                explode_value.append(0)                #explode_value값에 0 대입
        
                                                       #원그래프 Figure 생성, high_values대입, labels에 high_keys값 대입, explode에 explode_value값 대입, autopct는 비율표시        
        plt.pie(high_values, labels=high_keys, explode=explode_value, autopct='%.2f')

        plt.savefig('imsiTemp\\circle.jpg')            #imsiTemp 폴더에 원그래프.jpg 
        plt.close()                                    #그래프 Figure 닫기
        for i in range(0,len(high_keys)):
            print("%s : %d"%(high_keys[i],high_values[i]))
        image = Image.open("imsiTemp\\circle.jpg")     #image 변수에 circle.png파일 대입
        image.show()                                   #image 변수에 저장된 사진 출력

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

    if(os.path.isfile("imsiTemp\\wordcloud.jpg")):        #만약 circle.png라는 파일이 있으면
        image = Image.open("imsiTemp\\wordcloud.jpg")     #image 변수에 circle.png파일 대입
        image.show()                                   #image 변수에 저장된 사진 출력
    else:
        fc_keys=list(func_counter.keys())
        fc_values=list(func_counter.values())
        del_word_list=['[72시간세일]','[브랜드위크]','[위클리특가]','[오늘만이가격]','72시간세일','브랜드위크','위클리특가','오늘만이가격']

        for i in range(len(fc_keys)):
            fc_keys[i] = fc_keys[i].replace(' ', '')

        wordcloud_dict = dict(zip(fc_keys,fc_values))
        sorted_by_value = sorted(wordcloud_dict.items(), key=operator.itemgetter(1), reverse=True) # value(빈도수)값으로 내림차순 정렬
        t_mask = np.array(Image.open('image\\t5_2.jpg'))

        for sorted_dict in sorted_by_value:                     # 정렬된 상태의 이름과 빈도수 출력
            print("%s : %d"%(sorted_dict[0],sorted_dict[1]))

        fontpath='C:\\Windows\\Fonts\\NGULIM.TTF'

        wc = WordCloud(
            background_color='white',
            relative_scaling=0.2, 
            mask=t_mask, stopwords=del_word_list, 
            colormap ="Greens",
            font_path = fontpath

        ).generate(str(sorted_by_value))
        plt.figure(figsize=(8,8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.savefig('imsiTemp\\wordcloud.jpg')
        plt.close()
        wordcloud_img=Image.open('imsiTemp\\wordcloud.jpg')
        wordcloud_img.show()