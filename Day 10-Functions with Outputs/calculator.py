from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

op = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

def calcFunction():
    print(logo)
    calcContinue = True
    startOver = True
    num1 = float(input("First number: "))
    for key in op:
            print(key)

    while calcContinue:    
        operationChosen = input("Pick an operation from above: ")
        num2 = float(input("Second number: "))

        calFunction = op[operationChosen]
        answer = calFunction(num1, num2)

        print(f"{num1} {operationChosen} {num2} = {answer}")
        userContinue = input(f"Press 'yes' to continue with {answer},'no' to start over: ").lower()
        if userContinue == "no":
            calcContinue = False
            calcFunction()
        elif userContinue == "yes":
            num1 = answer

calcFunction()