def computeTotal(num , num2, operation):
    if operation == "+":
        return num + num2
    elif operation == "-":
        return num - num2
    elif operation == "*":
        return num * num2
    elif operation == '/':
        return num / num2
    else:
        return "Invalid"

while True:
    num = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    operation = input("Enter operation (+,-,*,/):")
    result = computeTotal(num , num2, operation)
    print("Result:", result)
    
    cont = input("Do you want to continue? (yes/quit):")
    if cont == "quit":
        break
