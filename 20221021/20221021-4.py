#閏年判斷
y = int(input("請輸入年份？"))

if ((y%4==0) and (y%100!=0)) or (y%400==0):
    print(str(y)+"是閏年")
else:
    print(str(y)+"不是閏年")