# 999 웹상의 반복되는 찾고자하는 요소들을 찾아 핸들링 색 찾기 게임 [btn.value_of_css_property('background-color') for btn in btns]
# from selenium import webdriver
# from pprint import  pprint
# import time
# from collections import Counter
#
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('http://zzzscore.com/color/')
# driver.implicitly_wait(300)
#
# btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
#
# def analysis():
#     btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
#     #pprint(btns_rgba)
#     result = Counter(btns_rgba)
#     #print(result)
#     for key, value in result.items():
#         if value == 1:
#             answer = key
#             break
#     else:
#         answer = None
#         print("정답을 찾을 수 없습니다.")
#
#     if answer :
#         index = btns_rgba.index(answer)
#         btns[index].click()
#
# if __name__ == "__main__":
#     start = time.time()
#     while time.time() - start <= 60:
#         analysis()


#유튜브 동영상 다운받기
# from pytube import YouTube
# yt = YouTube('https://www.youtube.com/watch?v=C0xIwnh8fOs') # 유튜브 영상 URL 입력
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



# 999 웹상의 반복되는 찾고자하는 요소들을 찾아 핸들링 1to50게임 숫자 빨리 찾기 find_elements_by_xpath
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://zzzscore.com/1to50')
# driver.implicitly_wait(300)
# num = 1
#
# btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
#
# for i in range(0, 50):
#     for j in range(0, len(btns)):
#         print('j =  ', j)
#         if num == int(btns[j].text):
#             btn = btns[j]
#             btn.click()
#
#             time.sleep(0.1)
#             # print(num, ' ', j)
#             num = num + 1
#             break
#     btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
#     print(num, ' ', j, '   ', btns[j-1].text)

# 전체에서 필요한 list를 얻고 list를 가지고 하나씩 뽑아서 분석
# import requests
# from bs4 import BeautifulSoup
#
# req = requests.get('http://tv.naver.com/r')
# raw = req.text
# html = BeautifulSoup(raw, 'html.parser')
#
# infos = html.select('div.cds_area > div')
# print(infos[0])
# for info in infos:
#     title = info.select_one('dt.title > a').text
#     chn = info.select_one('dd.chn').text[0:-1]
#     hit = info.select_one('span.hit').text
#     like = info.select_one('span.like').text
#
#     print(chn, '/', title, '/', hit, '/', like)

# 999 전체에서 통으로 원하는data를 얻고 거기서 list를 받아서 하나씩 분석 / 특수문자처리 / 이미지 웹에서 끌어와 저장 / 이미지 폴더에서 끌어오기 이미지 엑셀에 저장
# from bs4 import BeautifulSoup as bs
# from pprint import pprint
# import requests, re, os
# from urllib.request import  urlretrieve
# from openpyxl.drawing.image import Image
# from openpyxl import Workbook
#
# wb = Workbook()
# sheet1 = wb.active
# sheet1.title = '네이버 웹툰 완결편'
#
# try:
#     if not (os.path.isdir('image')):
#         os.mkdir(os.path.join('image'))
# except OSError as e:
#     if e.errno != errno.EEXITS:
#         print("폴더생성실패")
#         exit()
# url = 'https://comic.naver.com/webtoon/finish.nhn'
# html = requests.get(url)
# soup = bs(html.text, 'html.parser')
# all_data = soup.find('div', {'class':'list_area'})
#
# data_list = all_data.findAll('li')
#
# col = 1
# row = 1
# for data in data_list:
#     img_data = data.find('img')
#     img_src = img_data['src']
#     a_list = data.find('a')
#     title = a_list['title']
#     title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
#     link = "https//commic.naver.com" + a_list['href']
#     strong = data.find('strong').text
#
# #   urlretrieve(img_src, './image/'+title+'.gif')
#     img_title = './image/'+title+'.gif'
#     img_file = Image(img_title)
#     print(img_title)
#     img_file.anchor= 'C10'
#     #cell = sheet1.cell(row=10, column=1)
#     sheet1.add_image(img_file)
# #    sheet1.cell()
# #    col = col + 1
#     row = row + 1
#     break
# wb.save("./webtoon.xlsx")