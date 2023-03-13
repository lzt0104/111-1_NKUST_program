# pw = int(input("請輸入傳送密碼(6位數):"))

# while len(pw)>6:
#     ans = (pw*4)%7
#     ans2 = ans + ans*7*4


da={}
ans = []
for i in range(10):
    c=(i*4)%7
    dd={i:c}
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
        sb = input("取代字元與取代次數(字元 次數)").split(" ")
        print("字元"+str(sa)+"出現次數:",list(sa).count(sa))
        print("取代後字串:",st.replace(sa,sb[0],int(sb[1])))
    else:
        print("檢測結束")
        break

right = ['red','blue','red','green']
for i in range(10):
    hint = []
    user = input('依序輸入四個顏色(空白間隔)').split(' ')
    for color in range(4):
        if right.count(user[color])>0:
            if right[color]==user[color]:
                hint.insert(color,"1")
            elif right[color]!=user[color]:
                hint.insert(color,'2')
        elif right.count(user[color])<=0:
            hint.insert(color,'3')

    if hint.count('1')==4:
        print('正確答案')
        break
    elif hint.count('1')!=4:
        print(hint[0]+hint[1]+hint[2]+hint[3])


aa = []
for i in range(10):
    user = int(input('請輸入第'+str(i+1)+'個數字:'))
    aa.append(user)
aa.sort()
print('最小3個數字:',aa[0],',',aa[1],',',aa[2])
aa.reverse()
print('最大3個數字:',aa[0],',',aa[1],',',aa[2])






import random
list1 = []
for i in range(6):
    list1.append(random.randint(1,46))
print(list1)


da = {}
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



while True:
    st = input('輸入檢測字串(end結束):')
    if (st!='end'):
        sa = input('檢測的單一字元:')
        sb = input('取代字元與取代次數(字元 次數)').split(' ')
        print('字元'+str(sa)+'出現次數為:',list(st).count(sa))
        print('取代後字串:',st.replace(sa,sb[0],int(sb[1])))        
    else:
        print('檢測結束')
        break   



aa = input('處理方式(1)字典(2)串列:')
if (aa=='1'):
    ab = input('金 ')
    ac=input('銀 ')
    ad=input('銅 ')
    ae=input('優 ')
    dict1={'金':str(ab),'銀':str(ac),'銅':str(ad),'優':str(ae)}
    for a,b in dict1.items():
        print(a+'牌得到',b,'面')

elif(aa=='2'):
    ab = input('金 ')
    ac=input('銀 ')
    ad=input('銅 ')
    ae=input('優 ')
    list2=['金','銀','銅','優']
    list1 = [ab,ac,ad,ae]
    for i in range(len(list1)):
        print(list2[i]+'牌得到',list1[i],'面')
else:
    print('輸入錯誤')


right = ['red','blue','red','green']
for i in range(10):
    hint = []
    user = input('依序輸入四個顏色(空白間隔)').split(' ')
    for color in range(4):
        if right.count(user[color])>0:
            if right[color]==user[color]:
                hint.insert(color,"1")
            elif right[color]!=user[color]:
                hint.insert(color,'2')
        elif right.count(user[color])<=0:
            hint.insert(color,'3')

    if hint.count('1')==4:
        print('正確答案')
        break
    elif hint.count('1')!=4:
        print(hint[0]+hint[1]+hint[2]+hint[3])




