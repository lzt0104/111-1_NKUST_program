# pw = int(input("請輸入傳送密碼(6位數):"))

# while len(pw)>6:
#     ans = (pw*4)%7
#     ans2 = ans + ans*7*4


da={}
ans = []
for i in range(7):
    c=(i*4)%7
    dd={c:i}
    da.update(dd)
while True:
    aa=list(input('傳送密碼(6位數):'))
    if (len(aa)<6 or len(aa)>6):
        print('再輸入一次')
    elif len(aa)==6:
        for ii in range(6):
            ans.insert(ii,str(da.get(int(aa[ii]))))
        print(''.join(ans))
        break


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


while True:
    st = input("輸入檢測字元(end結束)")
    if st!="end":
        sa = input("檢測的單一字元:")
        
    else:
        print("檢測結束")
        break







f = open("data.txt",'r',encoding='cp950')

