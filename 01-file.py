# -*- coding: UTF-8 -*-

# Filename : 06-file.py
# author by : （学员ID)

# 目的:
# 掌握文件的打开、写入、读取

import os

# 写文件
filename = "test.txt"
f = open(filename, 'w')  # write 方式第一次写一行

text2write = "该文本会写入到文件中，看到我了吧！\n"
f.write(text2write)

text2write = "再写一行，又看到我了吧！\n"
f.write(text2write)

f.close()

# 读文件
f = open(filename, 'r') # readonly 方式读文件

print("第一个文件内容如下：")
text4read = f.read()
print(text4read)

f.close()

# 向文件追加内容
f = open(filename, 'a') # readonly 方式读文件

text2write = "这是追加的内容，看到我了吧！\n"
f.write(text2write)

f.close()

# 读文件
f = open(filename, 'r') # readonly 方式读文件

print("文件内容如下：")
text4read = f.read()
print(text4read)

f.close()
