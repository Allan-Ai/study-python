# -*- coding: UTF-8 -*-
'''
题目99：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
import string

question = "题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。"
print question

f = open("text1.txt", "rt")
a = f.readline()
f.close()

f = open("text2.txt", "rt")
b = f.readline()
f.close()

l = list(a + b)
l.sort()
s = ''
s = s.join(l)

f = open("text3.txt", "w")
f.write(s)
f.close()




