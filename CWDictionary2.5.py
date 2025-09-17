myStudents = {"s1":{
    "name":"Michael",
    "major":"Cybersecurity",
    "Year":"Freshmen",
    "credits":15,
    "gpa":0

}}



while True:
    print("1. Add a Student ")
    print("2. Delete a Student ")
    print("3. Edit a Student ")
    print("4. Print a Student ")
    print("5. Quit ")

    option = int(input("Select a option "))

    if option == "1":
        sid = input("Enter Student ID: ")
        nname = input("Name: ")
        mmajor = input("Major: ")
        yyear = input("Year: ")
        tcredits = int(input("TC: "))
        ggpa = input("GPA: ")

        myStudents.update({sid:{ #* *
            "name":nname,
            "major":mmajor,
            "year":yyear,
            "total credits":tcredits,
            "GPA":ggpa

        }})
        print(myStudents)

    elif option == "2":
        print("What student would you like to be delete? ")
        print(myStudents)
        del myStudents["s1" or "s2"]

    elif option == "3":
        sid = input("Enter the Student ID that needs to edited: ")
        myStudents.update({sid:{
            "name":nname,
            "major":mmajor,
            "year":yyear,
            "total credits":tcredits,
            "GPA":ggpa


        }})