"""
while 迴圈

while 條件式:
    程式區塊
"""

#範例1 1+2+....10
n = sum = 0
while (n<10):
    n += 1
    sum += n
print(sum)

#範例2 1~10偶數總和
n = 1
sum = 0
while n <=10:
    if n%2==0:
        sum = sum+n
    n = n+1
print(sum)

"""
利用While迴圈計算1~1000之間3的倍數，並且是奇數的總和
"""

n = 1
sum = 0
while n<=1000:
    if n%2 !=  0 and n%3 ==0:
        sum = sum+n
    n = n+1
print(sum)

#利用while寫出n!

n = int(input("請輸入n"))
sum = 1
while n>1:
    sum = sum*n
    n = n-1
print(sum)

# n! > M
pro = i =1
m = int(input("請輸入M?"))
while (pro<m):
    i = i+1
    pro = pro*i
print(i,"階層為",pro,"大於",m)

#輸入帳密，判斷正確與否。While

ac = str(123)
pd = str(456)
wac = str(input("請輸入帳號"))
wpd = str(input("請輸入密碼"))
while (ac != wac or pd != wpd) or (ac != wac and pd != wpd) or (ac == wac and pd == wpd) or (ac == wac and pd != wpd) or (ac != wac and pd == wpd):
    if ac == wac and pd != wpd:
        print("帳號正確，密碼錯誤")
    elif ac != wac and pd == wpd:
        print("帳號錯誤，密碼正確")
    elif ac != wac or pd != wpd:
        print("帳號密碼皆錯誤")
    else:
        print("帳號密碼正確")
    break




#輸入一整數，判斷其因數有哪些?並判斷是否為質數。while
n = int(input("請輸入整數"))
j = 2
i = 0
prime = True
while j<n:
    if(n%j==0):
        prime = False
        break
    j+=1
if prime:
    print(n,'是質數')
else :
    print(n,'不是質數')
    while i <= n:
        i += 1    
        if n%i ==0:
            print("有因數:",i,end = "\n")
            n = n/i
            i = 1
            pass
        else:
            pass


#輸入一整數，判斷其因數有哪些?並判斷是否為質數。while
n = int(input("請輸入整數"))
sum = 0
i = 1
print("因數有",end=" ")
while i<=n:
    if n%i == 0:
        sum += 1
        print(i,end=" ")
    i +=1
if sum>2:
    print("\n",n,"不是質數")
else:
    print("\n",n,"是質數")


