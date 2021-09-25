# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))
if bmi > 35:
    weightType = "clinically obese"
elif bmi > 30 and bmi < 35:
    weightType = "obese"
elif bmi > 25 and bmi < 30:
    weightType = "slighty overweight"
elif bmi > 18.5 and bmi < 25:
    weightType = "normal weight"
else:
    weightType = "underweight"
print(f"Your BMI is {bmi}, you are " + weightType)