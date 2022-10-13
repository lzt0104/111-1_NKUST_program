# 邏輯運算子
a = 5
b = 2
print(not(a==b))
print((a>=b))
print((a==b) and (a>=b))
print((a==b) or (a>=b))

# 複合指定運算子
i = 20
i += 2 #i = i+2
print(i)

# 字串運算
s = "123456789"
print(s)

print(s * 2) #複製字串
print(s[8]) #取值 []為索引值
print(s[-2])

print(s[1:5]) #切割字串[開始:結束(不包含本身):間隔]
print(s[:]) #全取
print(s[2:]) #從開始印到最後一個
print(s[:3]) #從結束(不包含本身)往前

print(s[:-2])
print(s[-4:-1])
print(s[3:-2])
print(s[2:8:2])
print(s[::-1]) #迴文
print(s[-1::-1]) #會等於[::-1]

#練習1 
t1 = int(input("請輸入第一次期中考成績？"))
t2 = int(input("請輸入第二次期中考成績？"))
t3 = int(input("請輸入期末考成績？"))
total = t1+t2+t3
av = total/3

print("總分為{}平均為{}".format(total,av))

#練習2
r = eval(input("請輸入幾尺？"))
u = eval(input("請輸入幾吋？"))
r1 = r*12
u1 = r1+u
cm = u1*2.54
print("轉換成{}公分".format(cm))

#練習3
num = eval(input("請輸入座號？"))

if num%5 ==0:
    team = num // 5
else:
    team = num // 5 +1

print("組別為{}".format(team))

#練習4
b = eval(input("請輸入購買罐數？"))
a = b // 12
c = b % 12
m1 = a * 200
m2 = c * 20
total = m1+m2
print("需花費{}".format(total))

# 判斷式 control
"""
1.單向判斷式
if 條件式:
    程式區塊
"""

#範例1(成績)
score = int(input("請輸入你的成績？"))
if score>=60:
    print("PASS")

#範例2(PW)
pw =  input("請輸入密碼")
if (pw == "1234"):
    print("歡迎光臨")

#範例3(天氣)
rain = input("明天會下雨嗎？(Y/N)")
if rain =="Y" or rain=="y" or rain=="會":
    print("請你攜帶雨具")

"""
2.雙向判斷
if 條件式:
    程式區塊1
else:
    程式區塊2
"""

#範例1(成績)
score = int(input("請輸入你的成績？"))
if score>=60:
    print("PASS")
else:
    print("未通過")

#範例2(PW)
pw =  input("請輸入密碼")
if (pw == "1234"):
    print("歡迎光臨")
else:
    print("密碼錯誤")

#範例3(判斷奇偶數)
n = int(input("請輸入一個正整數："))
if (n%2==0):
    print(f"數字{n}為偶數")
else:
    print(f"數字{n}為奇數")

#範例4(判斷三邊是否能構成三角形)
a = int(input("第一個邊的長度"))
b = int(input("第二個邊的長度"))
c = int(input("第三個邊的長度"))

if (a+b>c) and (b+c>a) and (c+a>b):
    print("可構成三角形")
    print("周長為：{}".format(a+b+c))
else:
    print("不可構成三角形")