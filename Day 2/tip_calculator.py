#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator!")
totalBill = float(input("How much was your total bill? $"))
tipPercentage = float(input("What percent would you like to tip them? "))
partySize = int(input("How many people are in your party? "))

finalBill = totalBill + (totalBill * (tipPercentage/100))
billSplit = finalBill / partySize

print(f"Each person should pay: {billSplit}")