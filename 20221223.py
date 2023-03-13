#items()

dic1 = {"金牌":26,"銀牌":34,"銅牌":20}
item1 = list(dic1.items())
for name,num in item1:
    print("得到的%s數量為%d面"%(name,num))

#set (集合)
s1 = {1,2,3,4}
s2 = set(('a',1,'b',2))
s3 = set(['apple','banana','apple']) #一樣的視為同一個元素
s4 = set(['apple','banana','apples'])

#add remove
s5 = set('tiger')
s5.add('s')
s5.remove('t')

s6 = list(s5)

#運算
a = set('12345')
b = set('4567')
print(a|b) #聯集
print(a&b) #交集
print(a-b) #差集
print(b-a)

#比較
a1 = set('tiger')
b1 = set('tigers')
print(a1 <= b1)
print(a1 < b1)

print(a1 >= b1)
print(a1 > b1)

a2 = set('tigers')
b2 = set('tigers')
print(a2 <= b2)
print(a2 < b2)

print(a2 >= b2)
print(a2 > b2)

#自訂函式
"""
def 函式名稱([參數1,參數2, ....]):
    程式區塊
    [return 回傳值1,回傳值2,....]
"""
def sayhello():
    print("歡迎光臨")

sayhello()

def min(a,b):
    if a>b:
        return b
    else:
        return a

print(min(12,4))

def getarea(w,h):
    area = w*h
    return area

print(getarea(10,3))

def getarea(w,h=12):
    area = w*h
    return area

print(getarea(10))
print(getarea(5,4))

#
p1 = "高雄科技大學，第一校區"
p2 = "高雄科技大學，燕巢校區"
s1 = set(p1)
s2 = set(p2)
print(s1 & s2) #共通都有的部分

#全域(gobal) & 區域(local) 變數
def scope():
    var1 = 1
    print(var1,var2)

var1=10
var2=20
scope()
print(var1,var2)


def scope():
    global var1,var2
    var1 = 1
    var2 = 2
    print(var1,var2)

var1=10
var2=20
scope()
print(var1,var2)

g = 5
def f1():
    print(g)
f1()

g = 5
def f2():
    #print(g)
    g = 10
    print(g)
f2()

#lambda函式
"""
lambda 參數清單(paramter list): 運算式

"""

def exp(x,y):
    return x ** y
exp(12,2)

exp1 = lambda x,y : x**y
exp1(12,2)

print((lambda x,y:x**y )(12,2))

def chop(x):
    if x<0.01:
        return 0
    else:
        return x

chop(0.001)
chop(1)

chop1 = lambda x:0 if x <.01 else x
chop1(0.001)
chop1(1)

#1.lambda 不需要定義名稱
#2.lambda 只能有一行運算式
#3.lambda 運算結束自動回傳結果

#檔案處理
"""
open(檔案名稱[,模式][,編碼])
模式:
1. r (read讀取) - 預設
2. w(write寫入) - 若檔案存在,內容會被覆蓋
3. a(add附加)

"""

content1 = '''hello
高科大12
welcome
'''
f = open('file1.txt','w',encoding='cp950')
f.write(content1)
f.close()

import locale
print(locale.getdefaultlocale())

f=open('file1.txt','r',encoding='cp950')
for line in f:
    print(line,end='')
f.close()

f = open('file1.txt','a',encoding='cp950')
f.write(content1)
f.close()

#readlines()
with open('file1.txt','r') as f:
    content=f.readlines()
    print(type(content))
    print(content)

#import
#1.
import random
random.randint(1,49) #產生整數


#2.
from random import *
randint(1,49)

#3.
import random as r #給予其他名稱
r.randint(1,49)

import guess as g
cop = g.figure_guess()
print(cop)

