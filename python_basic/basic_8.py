import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse
import json

class MovieSystem:
    url=''
    def __init__(self):
        self.url="https://www.kobis.or.kr/kobis/business/main/searchMainDailyBoxOffice.do"
    def movie_list(self):
        #문자열로 웹 데이터 읽기
        text_data=req.urlopen(self.url).read().decode("utf-8")
        #JSON변경
        json_data=json.loads(text_data)
        for movie in json_data:
            print(movie['rank'],movie['movieNm'],
                   movie['genre'])

    def movie_detail(self,rank):
        text_data = req.urlopen(self.url).read().decode("utf-8")
        # JSON변경
        json_data = json.loads(text_data)
        for movie in json_data:
            if rank==movie['rank']:
                print("영화제목:" + movie['movieNm'])
                print("상영일:" + movie['startDate'])
                print("장르:" + movie['genre'])
                print("등급:" + movie['watchGradeNm'])
                print("상영시간:" + movie['showTm'])
                print("순위:" + str(movie['rank']))
                print("줄거리:" + movie['synop'])
    def movie_test(self):
        pass

ms=MovieSystem()
ms.movie_list()
mno=int(input("영화 번호 선택:"))
ms.movie_detail(mno)