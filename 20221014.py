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
age = int(input("請輸入你的年齡"))