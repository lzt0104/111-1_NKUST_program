# 第一題
a = int(input("請輸入a的值："))
b = int(input("請輸入b的值："))
c = int(input("請輸入c的值："))
print("最大值為"+str(max(a,b,c)))

#第二題
k = int(input("請輸入物品重量？"))
if k<5 or k == 5:
    print("所需郵資為50元")
elif k>5 and k<=10:
    print("所需郵資為70")
elif k>10 and k<=15:
    print("所需郵資為90元")
elif k>15 and k<=20:
    print("所需郵資為110元")
else:
    print("超過20公斤無法寄送")

#第三題
m = int(input("請輸入購物金額："))
if m >=100000:
    print(str(m*0.8)+"元")
elif m >= 50000:
    print(str(m*0.85)+"元")
elif m >= 30000:
    print(str(m*0.9)+"元")
elif m >= 10000:
    print(str(m*0.95)+"元")
else:
    print(str(m)+"元")

#第四題