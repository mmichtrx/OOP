while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("select an Option: ")


    if option == "1":
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))
        print("The answer is:", num1 + num2)

    elif option == "2":
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))
        print("The answer is:", num1 - num2)

    elif option == "3":
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))
        print("The answer is:", num1 * num2)

    elif option == "4":
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))
        print("The answer is:", num1 / num2)

    elif option == "5":
        print("Exiting")
        break



