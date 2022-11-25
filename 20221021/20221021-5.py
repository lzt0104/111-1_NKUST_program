age = int(input("輸入受試者年紀："))
p1 = int(input("輸入P1："))
p2 = int(input("輸入P2："))
p3 = int(input("輸入P3："))
r = (p1+p2+p3-200)/10

if age >= 40:
    if r>=0 or r<=5:
        print(str(r)+"心肺功能優異")
    elif r >5 or r <=10:
        print(str(r)+"心肺功能優異")
    elif r > 10 or r<=15:
        print(str(r)+"心肺功能一般")
    elif r < 15 or r <=20:
        print(str(r)+"心肺功能不足")
    else:
        print("立即就醫評估")
elif age >= 18 and age <40:
    if r>=0 or r<=5:
        print(str(r)+"心肺功能優異")
    elif r >5 or r <=10:
        print(str(r)+"心肺功能一般")
    elif r > 10 or r<=15:
        print(str(r)+"心肺功能不足")
    elif r < 15 or r <=20:
        print(str(r)+"心肺功能不良")
    else:
        print("立即就醫評估")
else:
    print("不在題目範圍內")
