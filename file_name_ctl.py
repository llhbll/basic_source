from glob import glob
import os

file_list = glob("./data/*.xlsx")

for file in file_list :
    new_name = file.replace("복사복", "복").replace(" ", "")
    os.rename(file, new_name)

import sys

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")





