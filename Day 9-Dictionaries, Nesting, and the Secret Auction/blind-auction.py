from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
biddersLeft = True
bidderDict = {}

while biddersLeft:
  name = input("What is your name?: ")
  price = int(input("What is your bidding price?: "))
  bidderDict[name] = price
  usersLeft = input("Are there any other bidders left? Type 'yes' or 'no'").lower()
  if usersLeft == 'no':
    biddersLeft = False
  clear()

max = 0
person = ""
for key in bidderDict:
  if bidderDict[key] > max:
    max = bidderDict[key]
    person = key

print(f"Winner is '{person}' with a bid of ${max}!")