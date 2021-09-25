# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
monthsLeft = (90*12) - (age * 12)
weeksLeft = (90 * 52) - (age * 52)
daysLeft = (90 * 365) - (age * 365)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")
