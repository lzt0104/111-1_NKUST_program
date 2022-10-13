num = eval(input("請輸入座號？"))

if num%5 ==0:
    team = num // 5
else:
    team = num // 5 +1

print("組別為{}".format(team))
