"""
3.多項判斷式
if 條件式1:
    程式區塊1
elif 條件式2:
    程式區塊2
elif 條件式3:
    程式區塊3
....
else:
    程式區塊N
"""

#範例1(成績等第)
score = int(input("請輸入你的分數:"))
if score >= 90:
    print("甲等")
elif score >= 80:
    print("乙等")
elif score >= 70:
    print("丙等")
elif score >= 60:
    print("丁等")
else:
    print("您的成績未通過")

#範例2(電影等級)
age = int(input("請輸入你的年齡:"))
if (age < 6):
    print("普通級")
elif (age < 12):
    print("普通級、保護級")
elif (age < 18):
    print("限制級以外")
else:
    print("所有級別")

#範例3(成績等第(換方式))
score = float(input("請輸入您的成績(0-100):"))
if score < 0 or score > 100:
    print("輸入成績範圍有誤")
else:
    if 90 <= score:
        print("A")
    elif 80 <= score and score < 90:
        print("B")
    elif 70 <= score and score < 80:
        print("C")
    elif 60 <= score and score < 70:
        print("D")
    else:
        print("E")

#範例4(成績等第)-巢狀
score = float(input("請輸入您的成績(0-100):"))
if score < 0 or score > 100:
    print("輸入成績範圍有誤")
else:
    if 90 <= score:
        print("A")
    else:
        if score >= 80:
            print("B")
        else:
            if 70 <= score:
                print("C")
            else:
                if 60 <= score :
                    print("D")
                else:
                    print("E")

#練習1(國軍計算)
s = str(input("請輸入性別(男or女)："))
w = float(input("請輸入體重(公斤):"))
h = float(input("請輸入身高(公尺):"))
bmi = w / h**2

if s == "男":
    if bmi < 31 :
        print("合格")
    else:
        print("不合格")
else:
    if bmi < 26 :
        print("合格")
    else:
        print("不合格")

#練習2(座標判斷)
x = float(input("請輸入X座標："))
y = float(input("請輸入y座標："))

if x > 0 and y>0:
    print("第I象限")
elif x < 0 and y>0:
    print("第II象限")
elif x < 0 and y <0:
    print("第III象限")
else:
    print("第IV象限")

#練習3(熱量計算)
a = int(input("請輸入每日活動量(1:輕度,2:中度,3:重度)："))
h = float(input("請輸入身高(公尺):"))
w = float(input("請輸入體重(公斤):"))
bmi = w / h**2
hot = 0

if a == 1:
    if 24 <= bmi <27:
        hot = 25*w
    elif 18.5 <= bmi < 24:
        hot = 30*w
    else:
        hot = 35*w
elif a == 2:
    if 24 <= bmi <27:
        hot = 30*w
    elif 18.5 <= bmi < 24:
        hot = 35*w
    else:
        hot = 40*w
else:
    if 24 <= bmi <27:
        hot = 35*w
    elif 18.5 <= bmi < 24:
        hot = 40*w
    else:
        hot = 45*w

print("BMI為{}".format(bmi))
print("所需熱量為{:.2f}".format(hot))
