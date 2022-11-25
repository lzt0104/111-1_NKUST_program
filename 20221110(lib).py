n1 = int(input())
nsm = 0
sm = 0

if n1 <= 120:
    print("Summer Month:%.2f"%(n1*2.10))
    print("None Summer Month:%.2f"%(n1*2.10))
elif 121<=n1<=330:
    print("Summer Month:%.2f"%((n1*2.10)+(n1-120)*3.02))
    print("None Summer Month:%.2f"%((n1*2.10)+(n1-120)*2.68))
elif 331<=n1<=500:
    print("Summer Month:%.2f"%((n1-330)*4.39+(330-120)*3.02+120*2.10))
    print("None Summer Month:%.2f"%((n1-330)*3.61+(330-120)*2.68+120*2.10))
elif 501<=n1<=700:
    print("Summer Month:%.2f"%((n1-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("None Summer Month:%.2f"%((n1-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))
else:
    print("Summer Month:%.2f"%(((n1-700)*5.63+(700-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10)))
    print("None Summer Month:%.2f"%(((n1-700)*4.50+(700-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10)))



a = int(input("請輸入國文成績:"))
b = int(input("請輸入數學成績:"))
c = int(input("請輸入英文成績:"))
sumt = a+b+c
ave = sumt/3
print("成績總分：%d，平均成績：%.2f"%(sumt,ave))





a=int(input('請輸入一個正整數(<10):'))+1

for i in range(a):
    for s in range(i):
        print(i+(i*s) , end=' ')
    print()


month = int(input())
if month>=3 and month<=5:
    print("Spring")
elif month>=6 and month<=8:
    print("Summer")
elif month>=9 and month<=11:
    print("Autumn")
else:
    print("Winter")


a = input("")
b = input("")
c = input("")

if a+b>c and b+c>a and c+a>b:
    print("fit")
else:
    print("unfit")


kg = float(input("請輸入體重"))
tall = float(input("請輸入身高"))

bmi = kg/tall**2

print("BMI為{}".format(bmi))
if bmi < 18:
    print("體重過輕")
elif  18<=bmi <24:
    print("體重正常")
elif 24<=bmi<27:
    print("體重過重")
else:
    print("體重肥胖")

x = float(input())
y = float(input())
z = float(input())

speed=z/1.6/((x/60)+(y/60/60))

print("Speed:{:.1f}".format(speed))

m = int(input())

if 3<= m <=5:
    print("Spring")
elif 6<=m <=8:
    print("Summer")
elif 9<=m <=11:
    print("Autumn")
else:
    print("Winter")


age = int(input("請輸入年齡"))
p1 = int(input(""))
p2 = int(input(""))
p3 = int(input(""))

r = (p1+p2+p3-200)/10

if 18<=age < 40:
    if 0 <= r <=5:
        print("%.1f 心肺功能優異"%(r))
    elif 5<r<=10:
        print("%.1f 心肺功能一般"%(r))
    elif 10<r<=15:
        print("%.1f 心肺功能不足"%(r))
    elif 15<r<=20:
        print("%.1f 心肺功能不良"%(r))
    else:
        print("%.1f 立即就醫評估"%(r))
elif age >= 40:
    if 0 <= r <=5:
        print("%.1f 心肺功能優異"%(r))
    elif 5<r<=10:
        print("%.1f 心肺功能優異"%(r))
    elif 10<r<=15:
        print("%.1f 心肺功能一般"%(r))
    elif 15<r<=20:
        print("%.1f 心肺功能不足"%(r))
    else:
        print("%.1f 立即就醫評估"%(r))
else:
    print("不在題目範圍內")



act = int(input("請輸入每日活動量(1:輕度,2:中度,3:重度)："))
t = float(input("請輸入身高(公尺)"))
k = float(input("請輸入體重(公斤)"))
h = 1
bmi = k/t**2

if 35<=bmi:
    if act == 1:
        h = 25*k
    elif act ==2:
        h = 30*k
    else:
        h = 35*k
elif 30<=bmi<35:
    if act == 1:
        h = 25*k
    elif act ==2:
        h = 30*k
    else:
        h = 35*k
elif 27<=bmi<30:
    if act == 1:
        h = 25*k
    elif act ==2:
        h = 30*k
    else:
        h = 35*k
elif 24<=bmi<27:
    if act == 1:
        h = 25*k
    elif act ==2:
        h = 30*k
    else:
        h = 35*k
elif 18.5<=bmi<24:
    if act == 1:
        h = 30*k
    elif act ==2:
        h = 35*k
    else:
        h = 40*k
else:
    if act == 1:
        h = 35*k
    elif act ==2:
        h = 40*k
    else:
        h = 45*k

print("BMI為{}".format(bmi))
print("每日所需熱量%.1f"%(h))