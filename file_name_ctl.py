
# 숫자로만 된 일시 file명을 보기좋은 file명으로 변경
# from glob import glob
# import os
#
# # file_list = glob(r"C:\Users\pc\Downloads\20200712\2020*.jpg")
# Base_Dir = (r"C:\Users\pc\Downloads\source")
# file_list = os.listdir(Base_Dir)

# for file in file_list :
#     new_name = file[0:4] + '년 ' + file[4:6] + '월 ' + file[6:8] + '일 ' + file[8:]
#     to_file = os.path.join(Base_Dir, new_name)
#     from_file = os.path.join(Base_Dir, file)
#     os.rename(from_file, to_file)

# for (path, dir, files) in os.walk(r"C:\Users\pc\Downloads\Photos"):
#     for file in files:
#         new_name = file[0:4] + '년 ' + file[4:6] + '월 ' + file[6:8] + '일 ' + file[8:]
#         to_file = os.path.join(path, new_name)
#         from_file = os.path.join(path, file)
#         os.rename(from_file, to_file)


# 폴더 이동
# idx = 2 # 폴더이름
# for file in file_list :
#     new_dir = "C:\\Users\\pc\\Downloads\\Photos\\" + str(idx)
#     idx  = idx + 1
#     to_file = os.path.join(new_dir, file)
#     from_file = os.path.join(Base_Dir, file)
#     # print(from_file, to_file)
#     os.rename(from_file, to_file)

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

