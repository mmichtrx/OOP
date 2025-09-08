myList = []
x = 3

while 1:
    print("1. Append to the list")
    print("2. Remove from the list")
    print("3. Pop an element from the list")
    print("4. Display the List")
    print("5. Quit")
    option = input("Enter the number choice: ")

    if option == "1":
        myList.append(10)
        print("List has been appended")
    elif option == "2":
        print("What would you like to be removed? ")
        myList.remove(x)
        print("Has been removed.")
    elif option == "3":
        myList.pop()
        print("Element has been popped from the list.")
    elif option == "4":
        print(myList)
        print("The list has been displayed")
    elif option == "5":
        break