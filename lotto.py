import pandas as pd
import requests
from tqdm import tqdm
import json

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
    print("1부터 46까지 숫자를 중복없이 6자리 입력하세요 : ")
    num_str = input()
    aa = num_str.split()
#    aa = map(int, num_str.split()) #리스트의 문자열을 int형으로

    return aa

def lotto_match(my_num, lotto_list):
    cnt_1 = cnt_2 = cnt_3 = cnt_4 = cnt_5 = cnt_6 = 0
    for lotto_num in lotto_list:
        print(lotto_num[0], "회차 : 당첨번호 = ", lotto_num[1:7])

        match_num = my_num.intersection(set(lotto_num[1:7]))
        if len(match_num) == 6:
            print("-----------------1등입니다.------------------")
            cnt_1 += 1
        elif len(match_num) == 5 and match_num.intersection(set(lotto_num[7:8])):
            print("-----------------2등입니다.")
            cnt_2 += 1
        elif len(match_num) == 5:
            print("3등입니다. : ", match_num)
            cnt_3 += 1
        elif len(match_num) == 4:
            print("4등입니다.", match_num)
            cnt_4 += 1
        elif len(match_num) == 3:
            print("5등입니다.", match_num)
            cnt_5 += 1
        else:
            print("꽝입니다.")
            cnt_6 += 1
    print("꽝 : ", cnt_6, "회", "  5등 : ", cnt_5, "회", "  4등 : ", cnt_4, "회", "  3등 : ", cnt_3, "회", "  2등 : ", cnt_2, "회", "  1등 : ", cnt_1, "회")

my_num = input_my_lotte_num()
aaa  = Num_Chk(my_num)
if  aaa == '1':
    my_num_int = map(int, my_num)
    set_my_num = set(my_num_int)
    df_aa = getLottoWinInfo(50, 150)
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