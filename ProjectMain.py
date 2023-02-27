#환경설정
'''
1. 환경 : VSCode ,Jupyter notebook
2. https://code.visualstudio.com/docs/?dv=win(vscode 실행시)
2-1. ipykernel 설치 (※Jupyter notebook으로 실행시)
3. 파이썬 3.10.10 64bit (https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)
-> Add python.exe to Path 체크 후 install Now
'''
#%%
from module import moduleinstall
moduleinstall() # 모듈 통합 설치
from project import*
import auto # 1시간마다 20개씩 자동으로 크롤링하는 모듈
print("\n\t\t\t2조 : 전장현 // 이지운 // 김민수 // 장윤종 // 장기헌")

liYES=['y',"yes","Y","YES","Yes","네","예","넵","옙","ㅔ","ㅇ","ㅇㅋ","그래","그래요","그래용","ㅛ"]
liNO=["n","no","N","NO","No","아니요","x","X","ㄴ","아니","싫어","싫어요","안할래요","안 할래요","ㅜ"]

while(True):
    print('*'*100)
    print("\t\t\t\t무신사 쇼핑몰의 데이터 수집 및 분석") 
    print('*'*100,'\n')
    print("1) 데이터 크롤링 이후 축적") # bs4
    print("2) 02/21~23(3)일간 최대 많이 나온 검색어 상위 20") 
    print("3) 수집한 검색어의 빈도수 워드 클라우드") 
    print("4) 3일간 검색어 순위 막대 그래프") 
    print("5) 상품 검색 후 브랜드 워드클라우드") #셀레니움
    print("6) 상품 검색 후 브랜드 원 그래프") 
    print("0) 종료\n")

    createFolder() # 폴더 자동생성
    toKorean() # 한글화

    try:
        in_num=int(input("보고싶은 메뉴의 번호를 입력하세요.(종료:0)\n"))
        if(in_num==1):
            auto.auto_save_hour()   # 1시간 마다 데이터 자동축적

        # 3일간 최대 많이 나온 검색어 상위 20
        elif(in_num==2):
            searchTop(fileToCounter())  # 빈도수 상위 20개의 검색어

        elif(in_num==3): # 검색어-빈도수 워드클라우드
            mkWordCloud(fileToCounter()) # 파일에서 읽은 데이터 값 워드클라우드 생성

            s=input("이미지를 저장하시겠습니까? y/n ")
            if(s in liYES):
                print("고정된 값이므로 저장된 이름은 search_frequncy_wc.jpg로 고정입니다.")
                saveImg(in_num,'') # saveImg폴더안에 이미지 저장
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print() # 줄 띄우기
            elif(s in liNO):
                print("저장하지 않습니다.")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()

            else:
                print("잘못 입력하셨습니다.(저장하지 않습니다.)")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()


        elif(in_num==4): # 검색어-빈도수 막대그래프
            showBar(fileToCounter()) # 막대그래프 그리기
            s=input("이미지를 저장하시겠습니까? y/n ")
            if(s in liYES):
                print("고정된 값이므로 저장된 이름은 search_frequncy_stick.jpg로 고정입니다.")
                saveImg(in_num,'') # saveImg폴더안에 이미지 저장
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()
            elif(s in liNO):
                print("저장하지 않습니다.")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()

            else:
                print("잘못 입력하셨습니다.(저장하지 않습니다.)")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()
        
        # 상품 검색 후 브랜드 워드클라우드
        elif(in_num==5):
            mkWordCloud(searchBrand()) # 워드클라우드 생성
            print()
            s=input("이미지를 저장하시겠습니까? y/n ")
            if(s in liYES):
                while(True):
                    image_name1=input("저장하고 싶은 이미지파일명 : (확장자는 .jpg로 고정입니다.)") 
                    answer1=saveImg(in_num,image_name1) # answer변수에 리턴값 받아오기
                    if(answer1=='q'): # 받아온 answer변수의 값이 q일때 image_name값 다시 입력
                        continue  # 다시 반복
                    else: # 받아온 answer변수의 값이 no일때 이미지 저장
                        break # 반복 종료
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()
            elif(s in liNO):
                print("저장하지 않습니다.")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()
            else:
                print("잘못 입력하셨습니다.(저장하지 않습니다.)")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()

        # 상품 검색 후 브랜드 원 그래프
        elif(in_num==6):
            brandCircle()
            s=input("이미지를 저장하시겠습니까? y/n ")
            if(s in liYES):
                while(True):
                    image_name=input("저장하고 싶은 이미지파일명 : (확장자는 .jpg로 고정입니다.)")
                    answer=saveImg(in_num,image_name) # answer변수에 리턴값 받아오기
                    if(answer=='quit'): # 받아온 answer변수의 값이 quit일때 image_name값 다시 입력
                        continue # 다시 반복
                    else: # 받아온 answer변수의 값이 q이 아닐때 이미지 저장
                        break    # 반복 종료           
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()
            elif(s in liNO):
                print("저장하지 않습니다.")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()

            else:
                print("잘못 입력하셨습니다.(저장하지 않습니다.)")
                deleteImg(in_num) # imsiTemp폴더에 생성된 이미지 삭제
                print()               

        # 프로그램 종료
        elif(in_num==0):
            deleteFolder()              # imsiTemp폴더(내용있든 없든)삭제              
            print('프로그램을 종료합니다.')
            break
        
        elif(in_num < 0 or in_num > 6):
            print('0~6사이의 값으로 입력해주세요.\n')

        else:
            print("올바르지 않은 입력입니다.\n")

#예외처리
#
    except ValueError as value_e: # 에러를 value_e 객체로 변환
        e_list=[] # 에러 출력문 리스트
        e_list.append(str(value_e).split())
        e_munja = e_list[0][-1].split("'")
        
        if e_munja[1] == '' :
            # 스페이스바 일때
            print('공백입니다.\n')

        elif e_munja[1] == '' :
            # 공백일때
            print('공백입니다.\n')

        elif (ord('ㄱ') <= ord(e_munja[1][0])) and (ord(e_munja[1][0])<= ord('힣')) :
            # 한글을 입력했을때 오류 해결
            print('한글이 아닌 숫자 0~9를 입력해주세요.\n')

        elif (ord('A') <= ord(e_munja[1][0])) and (ord(e_munja[1][0])<= ord('z')) :
            # 영문을 입력했을때 오류 해결
            print('영어가 아닌 숫자 0~9를 입력해주세요.\n')
        
        elif (ord(e_munja[1][0])>=ord('!')) and (ord(e_munja[1][0])<=ord('/')) :
            # 특수문자열 첫번째가 ! 부터 / 까지 오류 해결
            print('특수문자가 아닌 1~9를 입력해주세요.\n')
        
        elif (ord(e_munja[1][0])>=58) and (ord(e_munja[1][0]))<=64 :
            # 특수문자열 첫번째가 : 부터 @ 까지 오류 해결
            print('특수문자가 아닌 1~9를 입력해주세요.\n')

        elif (ord(e_munja[1][0])>=91) and (ord(e_munja[1][0]))<=96 :
            # 특수문자열 첫번째가 [ 부터 ` 까지 오류 해결
            print('특수문자가 아닌 1~9를 입력해주세요.\n')

        elif not float(e_munja[1]).is_integer() :
            # 소수점을 입력했을때 오류 해결
            print('소숫점이 아닌 0~9를 입력해주세요.\n')

    except Exception:
        print("잘못된 입력입니다.")


# %%
