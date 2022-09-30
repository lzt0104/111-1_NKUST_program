# 課堂練習1
print("C111156104 劉政廷")
print("{0:3s}　{1:3s}　{2:2s}　{3:2s}　{4:2s}".format ("姓名","座號","國文","數學","英文"))
print("{0:3s}　{1:>4d}{2:>5d}{3:>5d}{4:>5d}".format ("林大明",1,100,87,79))
print("{0:3s}　{1:>4d}{2:>5d}{3:>5d}{4:>5d}".format ("陳阿中",2,74,88,100))
print("{0:3s}　{1:>4d}{2:>5d}{3:>5d}{4:>5d}".format ("張小英",11,82,65,8))

# 課堂練習2
print("C111156104 劉政廷")
print("{0:2s}　{1:3s}　{2:3s}　{3:3s}".format ("年度","所得稅","營業稅","證交稅"))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>.2f}".format ("2017",98.84,90.20,104.79))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>.2f}".format ("2016",83.00,110.50,82.45))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>.2f}".format ("2015",98.00,79.32,102.00))

# 輸入 input
"""
變數 = input([提示字串])
由input()所接收的值型別是字串
"""

score = input("請輸入您的程式設計成績為:")
print("您的程式設計成績為" + score)
print("您的程式設計成績為:{}".format(score))

# 使用型別轉換 int() str() float()
score1 = int(input("請輸入程式設計成績:"))
score2 = int(input("請輸入英文成績:"))
score3 = int(input("請輸入數學成績:"))

total = str(score1 + score2 + score3)
print(total)
print("您的總分是:" + str(total))

# 課堂練習3
print("C111156104 劉政廷")
name1 = str(input("請輸入姓名:"))
num1 = str(input("請輸入座號:"))
c1 = int(input("請輸入國文成績:"))
m1 = int(input("請輸入數學成績:"))
e1 = int(input("請輸入英文成績:"))
print("您輸入的資料為:姓名:{},座號{},國文{},數學{},英文{}".format (name1,num1,c1,m1,e1))
name2 = str(input("請輸入姓名:"))
num2 = str(input("請輸入座號:"))
c2 = int(input("請輸入國文成績:"))
m2 = int(input("請輸入數學成績:"))
e2 = int(input("請輸入英文成績:"))
print("您輸入的資料為:姓名:{},座號{},國文{},數學{},英文{}".format (name2,num2,c2,m2,e2))
name3 = str(input("請輸入姓名:"))
num3 = str(input("請輸入座號:"))
c3 = int(input("請輸入國文成績:"))
m3 = int(input("請輸入數學成績:"))
e3 = int(input("請輸入英文成績:"))
print("您輸入的資料為:姓名:{},座號{},國文{},數學{},英文{}".format (name3,num3,c3,m3,e3))
print("{0:3s}　{1:3s}　{2:2s}　{3:2s}　{4:2s}".format ("姓名","座號","國文","數學","英文"))
print("{0:3s}　{1:>3s}　{2:>5d}{3:>5d}{4:>5d}".format (name1,num1,c1,m1,e1))
print("{0:3s}　{1:>3s}　{2:>5d}{3:>5d}{4:>5d}".format (name2,num2,c2,m2,e2))
print("{0:3s}　{1:>3s}　{2:>5d}{3:>5d}{4:>5d}".format (name3,num3,c3,m3,e3))

# 課堂練習4
print("C111156104 劉政廷")
y1 = str(input("請輸入年度"))
o1 = float(input("請輸入所得稅"))
p1 = float(input("請輸入營業稅"))
l1 = float(input("請輸入證交稅"))
print("您輸入{}年的年度資料為:所得稅:{},營業稅:{},證交稅:{}".format(y1,o1,p1,l1))
y2 = str(input("請輸入年度"))
o2 = float(input("請輸入所得稅"))
p2 = float(input("請輸入營業稅"))
l2 = float(input("請輸入證交稅"))
print("您輸入{}年的年度資料為:所得稅:{},營業稅:{},證交稅:{}".format(y2,o2,p2,l2))
y3 = str(input("請輸入年度"))
o3 = float(input("請輸入所得稅"))
p3 = float(input("請輸入營業稅"))
l3 = float(input("請輸入證交稅"))
print("您輸入{}年的年度資料為:所得稅:{},營業稅:{},證交稅:{}".format(y3,o3,p3,l3))
print("{0:2s}　{1:3s}　{2:3s}　{3:3s}".format ("年度","所得稅","營業稅","證交稅"))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>6.2f}".format (y1,o1,p1,l1))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>6.2f}".format (y2,o2,p2,l2))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>6.2f}".format (y3,o3,p3,l3))

# 運算子
"""
1.算數運算子
+, -, *, /, %(餘數), //(商), **(指數)
2.比較運算子
==, <=, >=, <, >, !=(不等於)
3.邏輯運算子
not(反閘), and(及閘), or(或閘)
4.複合指定運算子
+=, -=, /=, %=, //=, **=
"""

# 數值運算
a = 5
b = 2

print(a+b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#範例1 (梯形面積)
top = float(input("請輸入上底長度為:"))
bottom = float(input("請輸入下底長度為:"))
heigh = float(input("請輸入高的長度為:"))
area = (top+bottom) * heigh / 2
print("梯形面積為:" + str(area))

#範例2 (溫度轉換)

c = float(input("請輸入攝氏溫度:"))
f = c * 9 / 5 + 32
print("華氏溫度:" + str(f))
print(f"攝氏{c}度等於華氏{f}度")
print("攝氏{1}度等於華氏{0}度".format(f,c))

#範例3 (BMI)
h = float(input("請輸入您的身高(cm):"))
w = float(input("請輸入您的體重(kg):"))
bmi = w / (h/100) **2
print("身高{}公分, 體重{}公斤, BMI值為{:.2f}".format(h,w,bmi))

# 比較運算子
x = 5
y = 2
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x > y)
print(x < y)