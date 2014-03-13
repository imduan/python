#!/usr/bin/python
# coding: utf-8

#打包成zip文件
import zipfile
f = zipfile.ZipFile('archive.zip','w',zipfile.ZIP_DEFLATED)
f.write('file_to_add.py')
f.close()
 
#从zip文件解包
import zipfile
zfile = zipfile.ZipFile('archive.zip','r')
for filename in zfile.namelist():
    data = zfile.read(filename)
    file = open(filename, 'w+b')
    file.write(data)
    file.close()
 
#把整个文件夹内的文件打包
import zipfile
f = zipfile.ZipFile('archive.zip','w',zipfile.ZIP_DEFLATED)
startdir = "c:\\mydirectory"
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        f.write(os.path.join(dirpath,filename))
f.close()
