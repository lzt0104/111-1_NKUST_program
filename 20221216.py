#刪除串列元素
#1.remove() / 串列名稱.remove()
list1 = ["燕巢","建工","第一","楠梓","旗津"]
list1.remove("第一")
print(list1)

#2.pop() / 串列名稱.pop() /後進先出
list2 = ["燕巢","建工","第一","楠梓","旗津"]
list2.pop() #無打值從最後一個值開始刪除
print(list2)

list2.pop(0)
print(list2)

#3.del / del 串列名稱(index) / del 串列名稱[開始:結束:間隔]
list3 = ["燕巢","建工","第一","楠梓","旗津"]
del list3[0]
print(list3)

list4 = ["燕巢","建工","第一","楠梓","旗津"]
del list4[0:4:2]
print(list4)


#sort() 由小排到大 / 串列名稱.sort()
list5 = [9,0,2,1]
list5.sort()
print(list5)

#reverse() 反轉 / 串列名稱.reverse()
list6 = [3,4,1,9]
list6.reverse()
print(list6)

#由大排到小 先sort再reverse
list6 = [3,4,1,9]
list6.sort()
list6.reverse()
print(list6)

#sorted
list6 = [3,4,1,9]
list7 = sorted(list6,reverse=True)
print(list6)
print(list7)

#總結
list7 = [1,2,3,4,5,6,7]
list7[1:4] #取出1到4-1的元素(element)
list7[1:4:2] #取出2.4
del list7[1:4] #刪除1到4-1的元素
del list7[1:4:2]

n = len(list7)
min(list7)
max(list7)

list7.index(3) #元素索引值
list7.count(5) #元素出現次數

list7.append(8) #加入元素在串列最後
list7.insert(3,9) #指定索引加入元素

list7.pop() #刪除/取出
list7.remove(6) #移除

list7.reverse() #反轉
list7.sort() #排序

#split() / 切割字串
s1 = "我們還小的時候，對於未來總有很多想像，想像自己是發明家、科學家、或是太空人，"
list8 = s1.split("，")
print(list8[0])
#replace()
list9 = s1.replace("未來","future")
print(list9)
#find()
list10 = s1.find("小")
print(list10)
#startswith() #判斷起值 是否包含某字串 (True/False)
s2 = "mailto:C111156104@nkust.edu.tw"
print(s2.startswith("mailto"))
print(s2.startswith("to"))
#endswith() #判斷終值 是否包含某字串 (True/False)
s3 = "mailto:C111156104@nkust.edu.tw"
print(s3.endswith("tw"))
print(s3.endswith("cn"))



#dict(字典)
#語法1: 字典名稱 = {key1:value1,key2:value2,key3:value3,key4:value4....}

dict1 = {}
dict2 = {"Hello":"哈囉","Google morning":"早安"}

#語法2: 字典名稱 = dict([[key1,value1],[key2,value2]])
dict3 = ([["Hello","哈囉"],["Google morning","早安"]])

#語法3: 字典名稱 = dict(key1=value1,key2=value2)
dict4 = dict(Hello="哈囉",Good_morning="早安")

dict5 = {"Hello":"哈囉","Google morning":"早安"}
print(dict5["Hello"])
print(dict5["Hell"]) #KeyError

print(dict5.get("Hell"))
print(dict5.get("Hell","不在字典內"))

#血型對應個性查詢
dict6 = {"A":"崇尚完美主義者的謹慎派","B":"充滿感情的行動家","O":"現實浪漫主義者","AB":"充滿矛盾的自信家"}
b_key = input("請輸入要查詢的血型名稱:")
b_value = dict6.get(b_key) 
if b_value == "None":
    print("沒有" + b_key + "血型")
else:
    print(b_key + "血型個性為:" + str(dict6[b_key]))


#字典維護
dict7 = {"侯先生":2,"王小姐":1,"吳小姐":4}
dict7["侯先生"]= 6 #改變value
dict7["侯先"] = 9 #key不存在，就會補上去

del dict7["侯先生"]
del dict7["侯"] #KeyError (key不存在出現的錯誤)

del dict7 #整個字典刪除
dict7.clear() #清空字典留下{}

#合併
dict8 = {"Hello":"哈囉"}
dict9 = {"Good_morning":"早安"}
dict8.update(dict9)

#如有重複的值 會覆蓋原有的值
dict8 = {"您好":"hello"}
dict9 = {"您好":"hi","早安":"good morning"}
dict8.update(dict9)

dict9 = {"您好":"hi","早安":"good morning"}
dict10 = dict9 #指向同一個字典物件
dict9["您好"] = "Hello" 

dict10 = {"您好":"hi","早安":"good morning"}
dict11 = dict10.copy() #
dict10["您好"] = "Hello"

#輸入名字查詢成績
dict_score = {"侯先生":90,"王小姐":87,"吳小姐":40}
name = input("請輸入欲查詢的姓名:")
if name in dict_score:
    print(name + "的成績為" + str(dict_score[name]))
else:
    score = input("輸入該生成績:")
    dict_score[name] = score
    print("成績字典內容為:" + str(dict_score))

#keys()
dict12 = {"侯先生":90,"王小姐":87,"吳小姐":40}
key1 = dict12.keys() #資料型態是dict_keys，所以不能以索引方式取得元素值
key1_list = list(dict12)
key1_1 = key1[0] #TypeError: 'dict_keys' object is not subscriptable
key1_1 = key1_list[0]


value1 = dict12.values()

