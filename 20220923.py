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

test = 2.2
print(type(test))

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

name1 = "Alex's iphone"

# 二、輸出(print)
"""
print(項目1,[項目2,....(,sep=分隔字元, end =結束字元)])
分隔字元預設' '(空白)，結束字元預設\n(換行)
"""

print(100 ,"智慧商務系", True )
print(str(100) + "智慧商務系" + str(True) )
print(100 ,"智慧商務系", True , sep="#" , end="\n")

"""
2-1 print() 命令參數格式化 (%)
print(項目 % (參數列))
%s (字串)
%d (整數)
%f (浮點數)
"""

print("%s的成績是%d分" % ("班代",80))
print("%5s的成績是%3d分" % ("班代",80))
print("%-5s的成績是%3d分" % ("班代",80))

print("我的體重有%f分" % (80))
print("我的體重有%-6.2f分" % (80.566))

"""
2-2 format
print(字串.format(參數列))
{}:參數位置
{i}: 索引值
{i:格式化指定}
對齊方式:>靠右 <靠左 ^置中
"""
print("班代的成績為80")
print("{}的成績為{}".format("班代",80))
print("{1}的成績為{0}".format("班代",80))
print("{0:^5s}的成績為{1}".format("班代",80))


"""
2-3 (f)
print(f字串)
"""

name3 = "班代"
score = 80
print(f"{name3}的成績為{score}")
print(f"{name3:>5}的成績為{score}")
print(f"{name3:x>5}的成績為{score:03}") #不足會補值