from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver.exe')
joonggonara_url = 'https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc'

driver.get(joonggonara_url)

# keyword = input("키워드 입력 : ")
search_input = driver.find_element_by_css_selector('input#topLayerQueryInput')
search_input.send_keys('갤럭시 탭')
search_button = driver.find_element_by_css_selector("form[name='frmBoardSearch'] > button")
search_button.click()
# time.sleep(5000)
# select_all = driver.find_element_by_css_selector("div#searchOptionSelectDiv > a")
# select_all.click()
# time.sleep(5000)
# select_button = driver.find_element_by_css_selector("div#searchOptionSelectDiv > ul > li:nth-child(2) > a")
# select_button.click()
# time.sleep(5000)
# listsize_button = driver.find_element_by_css_selector("div#listSizeSelectDiv > ul > li:nth-child(7) > a")
# listsize_button.click()

time.sleep(1)
driver.switch_to.frame("cafe_main")

title_list = []
writer_list = []
link_list = []
date_list = []
cost_list = []

for page in range(1, 20):
    list = driver.find_elements_by_css_selector('#main-area > div:nth-child(7) > table > tbody > tr')
    for item in list:
        title = item.find_element_by_css_selector('a.article').text
        writer = item.find_element_by_css_selector('a.m-tcol-c').text
        link = item.find_element_by_css_selector('a.article').get_attribute('href')
        cost =






