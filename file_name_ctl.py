
# 숫자로만 된 일시 file명을 보기좋은 file명으로 변경
# from glob import glob
# import os
#
# file_list = glob(r"C:\Users\sungshin\Documents\2020*.jpg")
# Base_Dir = (r"C:\Users\sungshin\Documents")
# # file_list = os.listdir(Base_Dir)
#
# for file in file_list :
#     new_name = file[28:32] + '년 ' + file[32:34] + '월 ' + file[34:36] + '일 ' + file[36:]
#     to_file = os.path.join(Base_Dir, new_name)
#     os.rename(file, to_file)


# from glob import glob
# import os
# 
# file_list = glob("./data/*.xlsx")
# 
# for file in file_list :
#     new_name = file.replace("복사복", "복").replace(" ", "")
#     os.rename(file, new_name)
#


# 회귀로 file명 찾기
# import sys
# 
# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == '.py':
#                     print(full_filename)
#     except PermissionError:
#         pass
# 
# search("c:/")
# 
# 

# image file 줄여서 다른 폴더에 넣기
# import os
# from PIL import Image
# 
# import openpyxl
# from xlsxwriter.utility import xl_col_to_name
# import glob
# 
# #img_list = glob.glob(r"C:\Users\sungshin\Documents\bbb\*.jpg")
# 
# Source_Dir = r"C:\Users\sungshin\Documents\bbb"
# img_list = os.listdir(Source_Dir)
# #
# Target_Dir = r"C:\Users\sungshin\Documents\ccc"
# num = 0
# for img_file in img_list:
#     img = Image.open(os.path.join(Source_Dir, img_file))
#     num = num + 1
#     file_name = str(num) + ".jpg"
#     img.resize((200,200)).save(os.path.join(Target_Dir, file_name))
# 


# 999 이미지 file 불러와 엑셀file에 집어 넣기
# import os
# #from PIL import Image
# from openpyxl.drawing.image import Image
# import openpyxl
# from xlsxwriter.utility import xl_col_to_name
# import glob
# 
# #img_list = glob.glob(r"C:\Users\sungshin\Documents\bbb\*.jpg")
# 
# Source_Dir = r"C:\Users\sungshin\Documents\bbb"
# # img_list = os.listdir(Source_Dir)
# #
# Target_Dir = r"C:\Users\sungshin\Documents\ccc"
# # num = 0
# # for img_file in img_list:
# #     img = Image.open(os.path.join(Source_Dir, img_file))
# #     num = num + 1
# #     file_name = str(num) + ".jpg"
# #     img.resize((200,200)).save(os.path.join(Target_Dir, file_name))
# 
# wb = openpyxl.load_workbook(r"E:\\2020학년도\\0. 공통업무\\기타\\운캠 지하101호 자산현황.xlsx")
# sheet = wb.active
# 
# row = 2
# col = 12
# 
# for row_data in sheet.rows:
#     val = sheet.cell(row, col).value
#     val1 = sheet.cell(row, col+1).value
#     if val is not None and sheet.cell(row, 14).value is None: # xl_col(0부터시작)....보다 +1 1부터 시작
#         file_name = str(val) + ".jpg"
#         img_file = Image(os.path.join(Target_Dir, file_name))
#         img_file.anchor = xl_col_to_name(13) + str(row)
#         # pprint('A' + str(col))
#         sheet.add_image(img_file)
#     if val1 is not None and sheet.cell(row, 15).value is None:
#         file_name = str(val1) + ".jpg"
#         img_file = Image(os.path.join(Target_Dir, file_name))
#         img_file.anchor = xl_col_to_name(14) + str(row)
#         # pprint('A' + str(col))
#         sheet.add_image(img_file)
#     row = row + 1
# wb.save(r"E:\\2020학년도\\0. 공통업무\\기타\\운캠 지하101호 자산현황.xlsx")
# 
# 
# 
# 
# 
# 
# 
