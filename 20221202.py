#for & while
#1.break

for i in range(1,6):
    print(i)
    if i == 4:
        break

i = 1
while (i<6):
    print(i)
    if i == 4:
        break
    i = i+1

#2.continue

for i in range(1,6):
    if i == 4:
        continue
    print(i)

i = 0
while (i<6):
    i = i+1
    if i == 4:
        continue
    print(i)

#資料儲存容器(tuple元組、list串列、dict字典、及set集合)    

#1.tuple
t1 = ()
print(t1)

t2 = 1,2,3

t3 = (1,2,3)

print(t3[0])
print(t3[2]) #index取出element元素

t3[2] = 4 #無法更改TypeError:'tuple' object

a, b, c = t3

#交換數字
a = 10
b = 20

a, b = b, a

t4 = (1,2,3,4)
t5 = (t4,5,6,7)

print(t5[0][0])
print(t5[0][2])
print(t5[1])
print(t5[3])

print(t5[0][6]) #IndexError

#2.list

list1 = []
list2 = [1,2,3,4]

list3 = ["第一校區","燕巢校區","楠梓校區"]
list4 = [1,2,3,"第一校區","燕巢校區","楠梓校區",True]

print(list4[0])
print(list4[4])

list4[3] = "旗津校區" 

list5 = [["Alex","12"],["Peko","13"],["Jeremy","14"]]
print(list5[0][0])
print(list5[1][0])
print(list5[2][0])  #前[]是人名，後[]是數字
print(list5[2][1])

print(list3[-2])#IndexError


print(list3[3])#IndexError

scores = [85,70,60]
print("英文成績: %d" % scores[0])
print("微積分成績: %d" % scores[1])
print("程設成績: %d" % scores[2])

for s in scores:
    print(s, end=" ")

print(len(scores))  #len=長度(length)

for s in range(len(scores)):
    print(scores[s],end=" ")

#範例1(科目成績)

subjects = ["英文","程設","微積分"]
scores = [89,77,56]
for i in range(len(scores)):
    print("%s成績為: %d 分" % (subjects[i], scores[i]))

#練習 範例1改為索引值由負的開始讀取
subjects = ["英文","程設","微積分"]
scores = [89,77,56]
for i in range(len(scores)-1,-1,-1):  #scores可跟subjects交換
    print("%s成績為: %d 分" % (subjects[i], scores[i]))

#index
print(scores.index(56))
print(subjects.index("程設"))

#count(數量)
scores = [89,77,56,100,100]
print(scores.count(100))
print(scores.count(90))

#增加串列元素
subjects = ["英文","程設","微積分"]
#1.append()
print(subjects.append("加數學"))
print(subjects)

#2.insert()
subjects.insert(1,"加數學")
print(subjects)

"""
索引值如果大於或等於串列個數，
就如同append()會將串列元素加在最後面
"""

subjects.insert(7,"加加數學")
print(subjects)

subjects = ["英文","程設","微積分"]
subjects.insert(-2,"嘎")
print(subjects)







a = int(input("請輸入學生的成績:"))
b = int(input("請輸入學生的成績:"))
c = int(input("請輸入學生的成績:"))
d = int(input("請輸入學生的成績:"))
e = int(input("請輸入學生的成績:"))
f = int(input("請輸入學生的成績:"))
scores = ["英文","程設","微積分"]
#1.append()
print(scores.append("加數學"))
print(scores)




scores = []

while True:
    score_input = input("請輸入學生的成績：")
    if score_input == "-1": 
        break
    
    scores.append(int(score_input))

score_len = len(scores)
scores = sum(scores)
avg = scores / score_len

print(f"共有 {score_len} 位學生")
print(f"本班總成績：{scores} 分，平均成績：{avg:.2f} 分")

print("共有%d位學生"%(score_len))
print("本班成績共%d分，平均成績%.2f分"%(scores,avg))