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
##999 이미지가 up 및 down시 회전오류 발생 시 잡아주기
# from PIL import Image, ExifTags
# import os
#
# for (path, dir, files) in os.walk(r"C:\Users\sungshin\Documents\aaaa"):
#     for file in files:
#         filename = os.path.join(path, file)
#         try:
#             image = Image.open(filename)
#             for orientation in ExifTags.TAGS.keys():
#                 if ExifTags.TAGS[orientation] == 'Orientation':
#                     break
#             exif = dict(image._getexif().items())
#
#             if exif[orientation] == 3:
#                 image = image.rotate(180, expand=True)
#             elif exif[orientation] == 6:
#                 image = image.rotate(270, expand=True)
#             elif exif[orientation] == 8:
#                 image = image.rotate(90, expand=True)
#
#             image.save(filename)
#
#         except (AttributeError, KeyError, IndexError):
#             # cases: image don't have getexif
#             pass

#image file에 텍스트 넣기
import os
from PIL import Image, ImageDraw, ImageFont

SrcDir = "E:\개인\python\사진"
img_list = os.listdir(SrcDir)
#
TgtDir = r"E:\개인\python\사진\결과물"

def wrtImg(file, data, w, h):

    srcImg = Image.open(os.path.join(SrcDir, file))
    TgtImgfile = os.path.join(TgtDir, file)
    txtPosiX =w
    txtPosiY = h

    fntSz = 15
    # fnt = ImageFont.truetype("sans-serif.ttf", fntSz, encoding="UTF-8")
    fnt = ImageFont.load_default()
    draw = ImageDraw.Draw(srcImg)
    draw.text((txtPosiY, txtPosiX), data, fill="white", font=fnt)
    srcImg.save(TgtImgfile)


for img_file in img_list:
    if os.path.isdir(os.path.join(SrcDir, img_file)):
        print("폴더")
    else:
        wrtImg(img_file, img_file, 10, 10)
