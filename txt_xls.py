import os
import numpy as np
import re
import xlwt as tx


# 正则表达式的匹配函数 方便提取每一行关键信息
def match(st):
    pattern = r'\d+(\.\d*)?'
    matchObj1 = re.search(pattern, st, re.M | re.I)
    matchObj2 = re.search(r'lossD: (.*?) .*', st, re.M | re.I)
    if matchObj1 and matchObj2:
        numObj1 = matchObj1.group() +' ' +matchObj2.group()
    else:
        numObj1 = "null"
    return numObj1

"""
#测试代码
str1 = "Step 5080/14760.0: lossD: -0.3051246404647827, lossG: 13.173877716064453"
str = match(str1)
print(str)
"""

# txt文件转化为xls
import sys
import xlwt #需要的模块

def txt2xls(filename,xlsname):  #文本转换成xls的函数，filename 表示一个要被转换的txt文本，xlsname 表示转换后的文件名
    f = open(filename)   #打开txt文本进行读取
    x = 0                #在excel开始写的位置（y）
    y = 0                #在excel开始写的位置（x）
    xls=xlwt.Workbook()
    sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True) #生成excel的方法，声明excel
    while True:  #循环，读取文本里面的所有内容
        line = f.readline() #一行一行读取
        if not line:  #如果没有内容，则退出循环
            break
        for i in line.split(' '):#读取出相应的内容写到x
                 item=i.strip()
                 if item == 'lossD:':
                     continue
                 if item == 'lossG:':
                     continue
                 else:
                     sheet.write(x,y,item)
                     y += 1 #另起一列
        x += 1 #另起一行
        y = 0  #初始成第一列
    f.close()
    xls.save(xlsname+'.xls') #保存

# txt2xls('newData1.txt','xls_n')

#按行读取文件,并写入新文件
def write_txt(filename_w):
    for line in open(filename_w,"r"):
        if line!="\n":
            data = match(line)
            if data!="null":
                with open("newData1.txt","a") as f:
                    f.write(data+"\n")


write_txt('UGAN.txt')
txt2xls('newData1.txt','xls')
"""
if __name__ == "__main__":
    filename = sys.argv[1]
    xlsname  = sys.argv[2]
    write_txt(filename)
    txt2xls('newData1.txt',xlsname)
"""

"""
#测试正则表达式
str1 = "Step 16700/98400: lossD: 0.007389731239527464, lossG: 0.2743561863899231"
str = match(str1)
print(str)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   
else:
   print ("No match!!")
"""
