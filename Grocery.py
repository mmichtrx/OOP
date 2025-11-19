import tkinter as tk
from tkinter import messagebox

class Customer:
    def __init__(self):
        self.user_id = ""
        self.username = ""
        self.pword = ""

    def add_customer(self):
        self.user_id = input("Enter the user ID: ")
        self.username = input("Enter a username: ")
        self.pword = input("Enter a password: ")

    def customer_login(self):
        self.username = idk
        self.pword = idk

class Employee:
    def __init__(self):
        self.employee_id = ""
        self.employee_password = ""
        self.employee_name = ""
        self.position = ""
        self.rate = 0.00
        self.time_worked = 0.0

    def add_employee(self):
        self.employee_id = input("Enter the employee ID: ")
        self.employee_password = input("Enter a password for new account: ")
        self.employee_name = input("Enter employee name: ")
        self.position = input("Enter position: ")
        self.rate = float(input("Enter rate: "))

    def employee_login(self):
        self.employee_id = input("")
        self.employee_password = input("idk")

    def employee_clockout(self):
        input("Enter the employee ID for who is clocking in: ")
        self.time_worked = float(input("Enter the amount of time that you worked: "))


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

class Login_App:
    def __init__(self, root):
        self.customer = Customer()
        self.employee = Employee()
        self.inventory = Inventory()
        self.root = root
        self.root.title("GUI")
        self.root.geometry("800x600")
        #self.root.resizeable(False, False)

        self.label = tk.Label(root, text="Enter LogIn ID:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        self.cust_login_btn = tk.Button(root, text="Customer LogIn", command=self.customer_login)
        self.cust_login_btn.pack(pady=5)
        self.empl_login_btn = tk.Button(root, text="Employee Login", command=self.employee_login)
        self.empl_login_btn.pack(pady=5)
        self.new_cust_btn = tk.Button(root, text="New Customer", command=self.add_customer)
        self.new_cust_btn.pack(pady=5)
        self.new_empl_btn = tk.Button(root, text="New Employee", command=self.add_employee)
        self.new_empl_btn.pack(pady=5)


    def add_customer(self):
        self.user_id = input("Enter the user ID: ")
        self.username = input("Enter a username: ")
        self.pword = input("Enter a password: ")

    def add_employee(self):
        self.employee_id = input("Enter the employee ID: ")
        self.employee_password = input("Enter a password for new account: ")
        self.employee_name = input("Enter employee name: ")
        self.position = input("Enter position: ")
        self.rate = float(input("Enter rate: "))

    def customer_login(self):
        print("")
        #self.username = idk
        #self.pword = idk

    def employee_login(self):
        self.employee_id = input("")
        self.employee_password = input("idk")


if __name__ == "__main__":
    root = tk.Tk()
    app = Login_App(root)
    root.mainloop()