# # 999 브라우저 띄우지 않고 data 가져오기
import requests # import urllib.request
from bs4 import BeautifulSoup

# url = 'http://cafe.daum.net/_c21_/bbs_read?grpid=2ouV&fldid=Erpk&contentval=00040zzzzzzzzzzzzzzzzzzzzzzzzz&datanum=248&page=1&prev_page=0&firstbbsdepth=&lastbbsdepth=zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz&listnum=20'
url = 'https://cafe.naver.com/ca-fe/ArticleRead.nhn?clubid=10050146&page=1&inCafeSearch=true&searchBy=0&query=%EA%B0%A4%EB%9F%AD%EC%8B%9C+%ED%83%AD&includeAll=&exclude=&include=&exact=&searchdate=all&media=0&sortBy=date&articleid=758683319&referrerAllArticles=true'
# url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

# 출처: https://hanswsw.tistory.com/7 [Han's Dev Log]'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
# webpage = requests.get(url).text  # webpage = urllib.request.urlopen(url)와 같음
webpage = requests.get(url, headers=headers)  # webpage = urllib.request.urlopen(url)와 같음
source = BeautifulSoup(webpage.text, 'html5lib')
print(source)
reviews = source.find_all('span', {'class': 'cost'})

for review in reviews:
    print(review)
    print(review.get_text().strip())



import requests # import urllib.request
from bs4 import BeautifulSoup

# base_url = 'http://movie.daum.net/moviedb/grade?movieId=2725&type=netizen&page={}'
#
# for n in range(77):
#     url = base_url.format(n + 1)
#     webpage = requests.get(url).text # webpage = urllib.request.urlopen(url)와 같음
#     source = BeautifulSoup(webpage, 'html5lib')
#     reviews = source.find_all('p', {'class': 'desc_review'})
#
#     for review in reviews:
#         print(review.get_text().strip())