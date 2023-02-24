def moduleinstall():
    try:
        import requests # 특정 웹사이트에 HTTP 요청을 보내 HTML 문서를 받아올 수 있는 라이브러리
        import bs4
        import selenium
        import matplotlib
        import wordcloud
        import numpy
        import schedule
    except:
        import sys
        import subprocess
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','requests'])
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','bs4'])
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','selenium'])
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','matplotlib'])
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','wordcloud'])
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','numpy'])
        subprocess.check_call([sys.executable,'-m','pip','install','--upgrade','schedule'])
        print('개발 환경 통합 설치 완료!\n')
    