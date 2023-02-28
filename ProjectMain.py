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
print("\n2조 : 전장현 // 이지운 // 김민수 // 장윤종 // 장기헌\n")

while(True):
    menu()

    createImsiFolder() # 임시폴더 자동생성
    createImgFolder() # 저장할 이미지 폴더 자동생성
    toKorean() # 한글화

    try:
        in_num=int(input("보고싶은 메뉴의 번호를 입력하세요.(종료:0)\n"))
        if(in_num==1):
            auto.autoSaveHour()   # 1시간 마다 데이터 자동축적
            print()
        # 3일간 최대 많이 나온 검색어 상위 20
        elif(in_num==2):
            print('\n'+'*'*50)
            print("  02/21~23(3)일간 최대 많이 나온 검색어 상위 20")
            print('*'*50,'\n')
            searchTop(fileToCounter())  # 빈도수 상위 20개의 검색어
            print()
        elif(in_num==3): # 검색어-빈도수 워드클라우드
            print('\n'+'*'*50)
            print("\t수집한 검색어의 빈도수 워드 클라우드")
            print('*'*50+'\n')
            mkWordCloud(fileToCounter()) # 파일에서 읽은 데이터 값 워드클라우드 생성
            answerStaticShow(in_num)
            print()

        elif(in_num==4): # 검색어-빈도수 
            print('\n'+'*'*50)
            print("\t3일간 검색어 순위 막대 그래프")
            print('*'*50)
            showBar(fileToCounter()) # 막대그래프 그리기
            answerStaticShow(in_num)
            print()
        
        # 상품 검색 후 브랜드 워드클라우드
        elif(in_num==5):
            print('\n'+'*'*50)
            print("\t상품 검색 후 브랜드 워드클라우드")
            print('*'*50)
            mkWordCloud(searchBrand()) # 워드클라우드 생성
            answerDynamicShow(in_num)
            print()
        # 상품 검색 후 브랜드 원 그래프
        elif(in_num==6):
            print('\n'+'*'*50)
            print("\t수집한 검색어의 빈도수 원 그래프")
            print('*'*50)

            brandCircle()
            answerDynamicShow(in_num)
            print()

        # 프로그램 종료
        elif(in_num==0):
            deleteimsiFolder()              # imsiTemp폴더(내용있든 없든)삭제              
            print('\n'+'*'*50)
            print("\t   이용해 주셔서 감사합니다.")
            print('*'*50)
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
