#迴圈(Loop)
"""

range()整數串列
range(終止值)
range(起始值,終止值,間隔值)


"""

list1 = range(5)
print(list(list1))
# [0, 1, 2, 3, 4]

list2 = range(3,8)
print(list(list2))
# [3, 4, 5, 6, 7]

list3 = range(3,8,2)
print(list(list3))
# [3, 5, 7]

list4 = range(8,3,-1)
print(list(list4))
# [8, 7, 6, 5, 4]

list5 = range(-2,4) #起始值為負值
print(list(list5))
# [-2, -1, 0, 1, 2, 3]

list6 = range(6,-2,-3)
print(list(list6))
# [6, 3, 0]

"""
for 迴圈

for 變數 in 串列:
    程式區塊
"""

list7 = ["燕巢校區","第一校區","旗津校區","建工校區","楠梓校區"]
for s in list7:
    print(s)

#1+....10
total = 0
for i in range(1,11):
    total += i
print(total)
#print(sum)

print(f'v2：{sum([i for i in range(1,11)])}')

total2 = 0
n = int(input("請輸入一個正整數n"))
for i in range(1,n+1):
    total2 += i
#print("1到{}的整數和為{}".format(n,total2))
print("1到%d的整數和為%d"% (n,total2))

#加總(起始、終值、及遞增/遞減值由使用者輸入)
b = int(input("請輸入加總起始值："))
e = int(input("請輸入加總終止值："))
s = int(input("請輸入加總遞增/遞減值："))
sum = 0
for a in range(b,e+1,s):
    sum += a
    print("i為",a,"加總結果為:",sum)

#99乘法表
for i in range (1,10):
    for j in range(1,10):
        product = i * j
        print("%d*%d = %2d  " % (i,j,product), end="")
    print()

#計算1*1+2*2+.....+n*n

sum =0
n = int(input("請輸入n的值:"))

if n>=1 and n<=1000:
    for i in range(1,n+1):
        product = i*i
        sum += product
    print(sum)
else:
    print("題目超過題目要求")

#求階層1!+2!+3!....+n!
sum = 1
total = 0
n = int(input("請輸入n的值:"))
for i in range(1,n+1):
    sum *= i
    total += sum
print(total)
