import os
import shutil


inidir = 'c:/Users/Sec55/Downloads'
fileList = os.listdir(inidir)
fdir = 'c:/Users/Sec55/Desktop/C-111DOCS'


for files in fileList:
    # print(files)
    shutil.move(inidir + '/' + files, fdir)
