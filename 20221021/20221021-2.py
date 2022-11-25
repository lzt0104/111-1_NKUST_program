#郵資
k = int(input("請輸入物品重量？"))
if k<5 or k == 5:
    print("所需郵資為50元")
elif k>5 and k<=10:
    print("所需郵資為70元")
elif k>10 and k<=15:
    print("所需郵資為90元")
elif k>15 and k<=20:
    print("所需郵資為110元")
else:
    print("超過20公斤無法寄送")