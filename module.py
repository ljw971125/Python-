def moduleinstall():
    try:
        import requests # 특정 웹사이트에 HTTP 요청을 보내 HTML 문서를 받아올 수 있는 라이브러리
        import bs4
        import selenium
        import matplotlib
        import wordcloud
        import numpy
        import schedule
        import webdriver-manager
    except:
        print("통합 모듈 설치를 시작합니다.")
        import sys
        import subprocess #모듈을 한번에 설치하기 위한 모듈
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','webdriver-manager`'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','requests'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','bs4'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','selenium'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','matplotlib'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','wordcloud'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','numpy'])
        subprocess.check_call([sys.executable,'-m','pip','install','-q','--upgrade','schedule'])
        print('환경설정 완료!\n')