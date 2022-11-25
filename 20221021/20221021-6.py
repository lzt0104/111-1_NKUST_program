k = float(input("請輸入體重(kg)："))
c = float(input("請輸入身高(M)："))

bmi = k/c**2

print("BMI為"+str(bmi))

if bmi >= 27:
    print("體重肥胖")
elif bmi >= 24 or bmi <27:
    print("體重過重")
elif bmi >=18 or bmi <24:
    print("體重正常")
else:
    print("體重過輕")
