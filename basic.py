# web 기본
# import time
# # 크롬 브라우저 조작을 위한 모듈
# from selenium import webdriver

# # 크롤링할 url 주소
# url = "https://www.instagram.com/explore/tags/python/"
#
# driver = webdriver.Chrome('chromedriver.exe')
# # 암묵적으로 웹 자원을 (최대) 5초 기다리기
# driver.implicitly_wait(5)
# # 크롬 브라우저가 실행되며 해당 url로 이동한다.
# driver.get(url)
# # 총 게시물 수를 클래스 이름으로 찾기
# totalCount = driver.find_element_by_class_name('g47SY').text
# print("총 게시물:", totalCount)

#999  웹상의 요소값 가져오기 selector
#from selenium import webdriver
#
# driver = webdriver.Chrome('./chromedriver')
#
# driver.get('http://v.media.daum.net/v/20170202180355822')
#
# # 클래스가 tit_view인 h3태그
# title = driver.find_element_by_css_selector("h3.tit_view")
# print (title.text)
# driver.quit()