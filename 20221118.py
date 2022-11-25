#break(跳出) & continue(跳過)

#break
for i in range(1,11):
    if(i==4):
        break
    print(i,end=" ")
print("break")

#continue
for i in range(1,11):
    if(i==4):
        continue
    print(i,end=" ")
print("continue")


n = int(input("請輸入一個數值："))
b = int(input("排除何數的倍數："))

for i in range(1,n+1):
    if(i%b==0):
        continue
    print(i,end=" ")

