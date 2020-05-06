# web 기본
# import time
# # 해시태그를 분석하기 위한 Twitter 모듈
# #from konlpy.tag import Twitter
# # 크롬 브라우저 조작을 위한 모듈
# from selenium import webdriver
# # 페이지 스크롤링을 위한 모듈
# from selenium.webdriver.common.keys import Keys
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