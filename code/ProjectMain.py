from module import moduleinstall
moduleinstall() # 모듈 통합 설치
from project import*
import os

import auto # 1시간마다 20개씩 자동으로 크롤링하는 모듈
print("\n2팀 : 전장현 // 이지운 // 김민수 // 장윤종 // 장기헌\n")

createImsiFolder() # 임시폴더 자동생성
createImgFolder() # 저장할 이미지 폴더 자동생성
toKorean() # 한글화


while(True):
    menu()
    try:
        in_num=int(input("보고싶은 메뉴의 번호를 입력하세요.(종료:0) : "))
        print()
        if(in_num==1):
            auto.autoSaveHour()   # 1시간 마다 데이터 자동축적
            print()
        elif(in_num==2): # 3일간 최대 많이 나온 검색어 상위 20
            doMenu(in_num,searchTop)
        elif(in_num==3): # 검색어-빈도수 워드클라우드
            doMenu(in_num,mkWordCloud)
        elif(in_num==4): # 검색어-빈도수 
            doMenu(in_num,showBar)
        # 상품 검색 후 브랜드 워드클라우드
        elif(in_num==5):
            doMenu(in_num,mkWordCloud)
        # 상품 검색 후 브랜드 원 그래프
        elif(in_num==6):
            doMenu(in_num,brandCircle)
        # 프로그램 종료
        elif(in_num==0):
            doMenu(in_num,'')
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

        if (len(e_munja[1])>1):
            print("한 자리 정수만 입력해주세요.")
        
        elif e_munja[1] == '' :
            # 스페이스바 일때
            print('공백입니다.\n')

        elif e_munja[1] == '' :
            # 공백일때
            print('공백입니다.\n')

        elif (ord('ㄱ') <= ord(e_munja[1][0])) and (ord(e_munja[1][0])<= ord('힣')) :
            # 한글을 입력했을때 오류 해결
            print('한글이 아닌 숫자 0~6을 입력해주세요.\n')

        elif (ord('A') <= ord(e_munja[1][0])) and (ord(e_munja[1][0])<= ord('Z')) :
            # 영문을 입력했을때 오류 해결
            print('영어가 아닌 숫자 0~6을 입력해주세요.\n')
        elif (ord('a') <= ord(e_munja[1][0])) and (ord(e_munja[1][0])<= ord('z')) :
            # 영문을 입력했을때 오류 해결
            print('영어가 아닌 숫자 0~6을 입력해주세요.\n')
        
        elif (ord(e_munja[1][0])>=ord('!')) and (ord(e_munja[1][0])<=ord('/')) :
            # 특수문자열 첫번째가 ! 부터 / 까지 오류 해결
            print('특수문자가 아닌 0~6을 입력해주세요.\n')
        
        elif (ord(e_munja[1][0])>=58) and (ord(e_munja[1][0]))<=64 :
            # 특수문자열 첫번째가 : 부터 @ 까지 오류 해결
            print('특수문자가 아닌 0~6을 입력해주세요.\n')

        elif (ord(e_munja[1][0])>=91) and (ord(e_munja[1][0]))<=96 :
            # 특수문자열 첫번째가 [ 부터 ` 까지 오류 해결
            print('특수문자가 아닌 0~6을 입력해주세요.\n')

            
        elif not float(e_munja[1]).is_integer() :
            # 소수점을 입력했을때 오류 해결
            print('소숫점이 아닌 0~6을 입력해주세요.\n')
            
        
    except FileNotFoundError:
        print("메뉴로 돌아갑니다.")
    except Exception:
        print("잘못된 입력입니다.")