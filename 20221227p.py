pw = int(input("請輸入傳送密碼(6位數):"))

while len(pw)>6:
    ans = (pw*4)%7
    ans2 = ans + ans*7*4


se = int(input("請輸入查詢方式(1.字典 2.串列):"))

if se == 1:
    aa = input("金:")
    ab = input("銀:")
    ac = input("銅:")
    ad = input("優:")
    dic = {"金牌":str(aa),"銀牌":str(ab),"銅牌":str(ac),"優勝":str(ad)}
    for a,b in dic.items():
        print(a+"得到"+b+"面")

elif se == 2:
    aa = input("金:")
    ab = input("銀:")
    ac = input("銅:")
    ad = input("優:")
    list1 = ["金牌","銀牌","銅牌","優勝"]
    list2 = [aa,ab,ac,ad]
    for i in range (len(list1)):
        print(list1[i]+"得到"+list2[i]+"面")
else:
    print("輸入錯誤")
