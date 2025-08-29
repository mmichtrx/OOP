number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

operator = input("+, -, *, /? ")

if operator == "+":
    print("The sum is:", number1+number2)
elif operator == "-":
    print("The sum is:", number1-number2)
elif operator == "*":
    print("The sum is:", number1*number2)
elif operator == "/":
    print("The sum is:", number1/number2)