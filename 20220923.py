# 一、變數與資料型態

"""
宣告變數
大小寫不同
名稱:大小寫英文、數字、中文(不建議)
第一個字母不能是數字
"""

from turtle import Turtle


X = 1  #C int float
y = 0.1
a = b = c = 0
age, name = 18 , "智慧商務系"

print(age,name)

"""
2.變數資料型態
整數(int)、浮點數(float)、字串(str)、布林(bool) False/True
查看資料型態type()
資料型態的轉換int(),float(),str()
"""

age = 2
justdoit = False
name = "Alex"
weight = 123.5
zipcode = "545"
msg = """
Alex
Rooney
Peko
"""

print(type(age))
print(type(name))

num1 = 8+True
num2 = 8+False
num3 = age + int(zipcode)
num4 = str(age) + zipcode

print(num1,num2,num3)
print(num4)
