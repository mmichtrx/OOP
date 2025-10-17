class Customer:
    def __init__(self):
        self.user_id = ""
        self.username = ""
        self.pword = ""

    def add_customer(self):
        self.user_id = input("Enter the user ID: ")
        self.username = input("Enter a username: ")
        self.pword = input("Enter a password: ")

class Employee:
    def __init__(self):
        self.employee_id = ""
        self.employee_name = ""
        self.position = ""
        self.rate = 0.00

    def add_emoplyee(self):
        self.employee_id = input("Enter the employee ID: ")
        self.employee_name = input("Enter employee name: ")
        self.position = input("Enter position: ")
        self.rate = float(input("Enter rate: "))

class Inventory:
    def __init__(self):
        self.product_id = ""
        self.product_category = ""
        self.amount = 0
        self.price = 0.00

    def add_inventory(self):
        self.product_id = input("Enter the product ID: ")
        self.product_category = input("Enter product category: ")
        self.amount = int(input("Enter amount: "))
        self.price = float(input("Enter price: "))

while 1:
    print("1. Customer Panel")
    print("2. Employee Panel")
    print("3. Inventory Panel")
    print("4. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        print("1. Add New User\n"
              "2. Log-In\n"
              "3. Log-Out\n"
              "4. Back to main menu")

        cust_option = int(input("Select option: "))

        if cust_option == 1:
            self.add_customer()


    elif option == 2:
        print("1. Add employee\n"
              "2. Clock-In\n"
              "3. Clock-Out\n"
              "4. Deliver\n"
              "5. Back to main menu")

        emp_option = int(input("Select an option: "))

        if emp_option == 1:
            self.add_emp()

    elif option == 3:
        print("1. Add to inventory\n"
              "2. Remove from inventory\n"
              "3. Adjust price\n"
              "4. Back to main menu")

    elif option == 4:
        break