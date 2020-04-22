


#웹상의 반복되는 찾고자하는 요소들을 찾아 핸들링 색 찾기 게임 [btn.value_of_css_property('background-color') for btn in btns]
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










#웹상의 반복되는 찾고자하는 요소들을 찾아 핸들링 1to50게임 숫자 빨리 찾기 find_elements_by_xpath
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