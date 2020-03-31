# import os
#
# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_file_name = os.path.join(dirname, filename)
#             if os.path.isdir(full_file_name):
#                 search(full_file_name)
#             else:
#                 ext = os.path.splitext(full_file_name)[-1]
#                 if ext == '.py':
#                     print(full_file_name)
#     except PermissionError:
#         pass
#
# search("c:/")


import os

for(path, dir, filenames) in os.walk("c:/"):
    for filename in filenames:
        ext = os.path.splitext(filename)[-1]
        if(ext == ".py"):
            print("%s%s" %(path, filename))
