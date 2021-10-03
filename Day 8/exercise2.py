#Write your code below this line 👇
def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
           isPrime = False
           break

    if isPrime:
        print(f"{number} is a prime number!")       
    else:
        print(f"{number} is not a prime number!")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
#n = int(input("Check this number: "))

#for n in range(100):
#    prime_checker(number=n)

n = int(input("Check this number: "))
prime_checker(number=n)