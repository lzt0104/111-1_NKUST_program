#購物打折
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