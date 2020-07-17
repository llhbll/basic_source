import pandas as pd
import requests
from tqdm import tqdm
import json
import random

def getLottoWinInfo(minDrwNo, maxDrwNo):
    drwtNo1 = []
    drwtNo2 = []
    drwtNo3 = []
    drwtNo4 = []
    drwtNo5 = []
    drwtNo6 = []
    bnusNo = []
    totSellamnt = []
    drwNoDate = []
    firstAccumamnt = []
    firstPrzwnerCo = []
    firstWinamnt = []

    for i in tqdm(range(minDrwNo, maxDrwNo+1, 1)):
        req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)
        req_lotto = requests.get(req_url)

#        lottoNo = req_lotto.json()
        lottoNo = json.loads(req_lotto.text)

        drwtNo1.append(lottoNo['drwtNo1'])
        drwtNo2.append(lottoNo['drwtNo2'])
        drwtNo3.append(lottoNo['drwtNo3'])
        drwtNo4.append(lottoNo['drwtNo4'])
        drwtNo5.append(lottoNo['drwtNo5'])
        drwtNo6.append(lottoNo['drwtNo6'])
        bnusNo.append(lottoNo['bnusNo'])
        totSellamnt.append(lottoNo['totSellamnt'])
        drwNoDate.append(lottoNo['drwNoDate'])
        firstAccumamnt.append(lottoNo['firstAccumamnt'])
        firstPrzwnerCo.append(lottoNo['firstPrzwnerCo'])
        firstWinamnt.append(lottoNo['firstWinamnt'])

        lotto_dict = {"추첨일":drwNoDate, "Num1":drwtNo1, "Num2":drwtNo2, "Num3":drwtNo3, "Num4":drwtNo4,
                      "Num5":drwtNo5, "Num6":drwtNo6, "bnsNum":bnusNo, "총판매금액":totSellamnt,
                      "총1등당첨금":firstAccumamnt, "1등당첨인원":firstPrzwnerCo, "1등수령액":firstWinamnt}
    df_lotto = pd.DataFrame(lotto_dict)

    return df_lotto
    ##출처##  [솜씨좋은장씨]

def Num_Chk(nums):
    for num in nums:
        if(int(num) <= 0) or (int(num) >= 46):
            return "잘못된 번호를 입력"
    return '1'

def input_my_lotte_num():
    print("1부터 46까지 구간 숫자를 중복없이 스페이스로 구분하여 6개 입력하세요 : (랜덤 6개 : r, 빠져나가기 : q)")
    num_str = input()
    six_list = num_str.split()
#    aa = map(int, num_str.split()) #리스트의 문자열을 int형으로

    return six_list

def lotto_match(my_num, lotto_list):
    cnt_1 = cnt_2 = cnt_3 = cnt_4 = cnt_5 = cnt_6 = 0
    for lotto_num in lotto_list:
        match_num = my_num.intersection(set(lotto_num[1:7]))
        if len(match_num) >= 3:
            print(lotto_num[0], "회차 : 추첨일자 = ", lotto_num[1:2], "  당첨번호 = ",  lotto_num[2:8],   "  보너스번호 = ",
                  lotto_num[8:9], "  1등 당첨인원 = ",lotto_num[11:12], "  1등 수령액 = ", format(int(lotto_num[12:13][0]), ','))

        if len(match_num) == 6:
            print("-----------------1등입니다.------------------")
            cnt_1 += 1
        elif len(match_num) == 5 and len(my_num.intersection(set(lotto_num[8:9])))  == 1:
            print("-----------------2등입니다.------------------")
            cnt_2 += 1
        elif len(match_num) == 5:
            print("------------------3등입니다.----------------- : ", match_num)
            cnt_3 += 1
        elif len(match_num) == 4:
            print("----------4등입니다.----------", match_num)
            cnt_4 += 1
        elif len(match_num) == 3:
            print("5등입니다.", match_num)
            cnt_5 += 1
        else:
            # print("꽝입니다.")
            cnt_6 += 1
    print("\n 꽝 : ", cnt_6, "회", "  5등 :", cnt_5, "회  ", "  4등 :", cnt_4, "회", "  3등 :", cnt_3, "회",
          "  2등: ", cnt_2, "회", "  1등 :", cnt_1, "회\n")
    if cnt_1 != 0 or cnt_2 != 0 or cnt_3 != 0:
        print("와우 3등이상 당첨되셨을 번호였네요!\n")

cnt = 0
while 1:
    my_num = input_my_lotte_num()
    if my_num[0][0] == 'q':
        break
    if my_num[0][0] == 'r':
        aaa = '1'
        tmp_set = set()
        while len(tmp_set) < 6:
            tmp_set.add(random.randrange(1, 46))
        my_num = list(tmp_set)
    else:
        aaa  = Num_Chk(my_num)
    if  aaa == '1':

        my_num_int = map(int, my_num)
        set_my_num = set(my_num_int)
        print(set_my_num)
    #    df_aa = getLottoWinInfo(1, 919) 로또사이트의api를 이용하여 로또당첨번호 읽어와서 df로
    #    df_aa.to_excel("lotto_list.xlsx")
        df_aa = pd.read_excel('lotto_list.xlsx', sheet_name='Sheet1')
        aa_list = df_aa.values.tolist()
        lotto_match(set_my_num, aa_list)
    else:
        print(aaa)


# print(aa_list)

# print(aa.index, aa.values[])
# lotto_old_list._combine_match_columns()
# for i in range(0, 3):
#     print(lotto_old_list.index[i])
#     print(lotto_old_list.columns[i][2])
##출처##  [솜씨좋은장씨]