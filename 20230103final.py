#讀檔
path="data.txt"
with open(path) as data:
    bloodStr=""
    blood_total=0
    heart_total=0
    for line in data.readlines():
        bloodStr+=line
    bloodStr=bloodStr.replace("\n",",")
    bloodDB=bloodStr.split(",")
    bloodDB=list(map(int,bloodDB))
    a=len(bloodDB)

    blood=[]
    for i in range(0,a,2):
        blood.append(bloodDB[i])
    for i in range(len(blood)):
            blood_total+=blood[i]
    blood_press_average=blood_total/len(blood)

    heart=[]
    for i in range(1,a,2):
        heart.append(bloodDB[i])
    for i in range(len(heart)):
            heart_total+=heart[i]
    heart_average=heart_total/len(heart)

    blood.sort()
    heart.sort()

    print("血壓平均: %.2f" %(blood_press_average))
    print("血壓最大值:",blood[-1])
    print("血壓最小值:",blood[0])
    print()
    print("心跳平均: %.2f" %(heart_average))
    print("心跳最大值:",heart[-1])
    print("心跳最小值:",heart[0])

#檢測字串
while True:
    st = input("輸入檢測字串(end結束):")
    if (st!="end"):
        sa = input("檢測的單一字元:")
        sb = input("取代字元與取代次數(字元 次數)").split(" ")
        print("字元"+str(sa)+"出現次數為:",list(st).count(sa))
        print("取代後字串:",st.replace(sa,sb[0],int(sb[1])))        
    else:
        print("檢測結束")
        break   

#金銀銅
aa = input("處理方式(1)字典(2)串列:")
if (aa=="1"):
    ab = input("金 ")
    ac=input("銀 ")
    ad=input("銅 ")
    ae=input("優 ")
    dict1={"金":str(ab),"銀":str(ac),"銅":str(ad),"優":str(ae)}
    for a,b in dict1.items():
        print(a+"牌得到",b,"面")

elif(aa=="2"):
    ab = input("金 ")
    ac=input("銀 ")
    ad=input("銅 ")
    ae=input("優 ")
    list2=["金","銀","銅","優"]
    list1 = [ab,ac,ad,ae]
    for i in range(len(list1)):
        print(list2[i]+"牌得到",list1[i],"面")
else:
    print("輸入錯誤")

#RBRG
right = ["red","blue","red","green"]
for i in range(10):
    hint = []
    user = input("依序輸入四個顏色(空白間隔)").split(" ")
    for color in range(4):
        if right.count(user[color])>0:
            if right[color]==user[color]:
                hint.insert(color,"1")
            elif right[color]!=user[color]:
                hint.insert(color,"2")
        elif right.count(user[color])<=0:
            hint.insert(color,"3")

    if hint.count("1")==4:
        print("正確答案")
        break
    elif hint.count("1")!=4:
        print(hint[0]+hint[1]+hint[2]+hint[3])


#import

import random
list1 = []
for i in range(6):
    list1.append(random.randint(1,46))
print(list1)