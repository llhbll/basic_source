
# 파일 읽고 쓰기
# import  sys
#
# option = sys.argv[1]
#
# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt', 'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()
# elif option == '-v':
#     f = open('memo.txt', 'r')
#     memo = f.read()
#     f.close()
#     print(memo)

# pandas Seris
# from pandas import Series
#
# data = [100, 200, 300, 400]
# date = ['2018-08-01', '2019-08-01', '2020-08-01', '2020-08-02']
# s = Series(data, index = date)
# print(s[[0, 2]])

# pandas dataframe
# from pandas import DataFrame
#
# data = {'open':[100, 200], 'high':[110, 210]}
# df = DataFrame(data, index=['2018-01-01', '2018-01-02'])
#
# print(df)

# import pandas as pd 데이타프레임 data추가 엑셀에 읽고 쓰기
#
# df = pd.read_excel("test.xlsx")
# df = df.set_index('date')
# f_title = df["d_title"] * 2
# df["f_title"] = f_title
# df.to_excel("out.xlsx")
# print(df.iloc[2])

# import pandas as pd
# url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
# df = pd.read_html(url)
# df[0] = df[0].dropna(axis=0)
# df[0].to_excel("out.xlsx")

