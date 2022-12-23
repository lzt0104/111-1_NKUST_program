y = int(input("請輸入西元年:"))

an = ['虎','兔','龍','蛇','馬','羊','猴','雞','狗','豬','鼠','牛']
c = y%2010
if 0<=c<=12:
    print(an[c])


M = int(input("請輸入階乘值M"))
n=1
total=1

while total<M:
    total*=n
    n+=1

print("超過M為%d的最小階層N值為：%d"%(M,n-1))
