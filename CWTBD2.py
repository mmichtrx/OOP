class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0.00

    def debit_from(self):
        self.balance -= float(input("Enter Amount To Send:  "))

    def credit_to(self):
        self.balance += float(input("Enter Amount To Earned:  "))

    def add_customer(self):
        self.cid = input("Enter Customer ID:    ")
        self.acc_no = input("Enter Account Number:  ")
        self.cname = input("Enter Customer Name:   ")
        self.phone = input("Enter Phone Number: ")
        self.emailid = input("Enter Email ID:   ")
        self.balance = float(input("Enter Balance:  "))

    def display_all(self):
        print("Customer ID:", self.cid)
        print("Account Number:", self.acc_no)
        print("Customer Name:", self.cname)
        print("Phone Number:", self.phone)
        print("Email ID:", self.emailid)
        print("Balance:", self.balance)




c1 = Customer()
c2 = Customer()

c1.add_customer()
c2.add_customer()

c1.debit_from()
c2.credit_to()

c1.display_all()
c2.display_all()