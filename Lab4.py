class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0.00
        self.card = []

    def debit_from(self):
        self.balance -= float(input("Enter Amount To Send:  "))

    def credit_to(self):
        self.balance += float(input("Enter Amount To Earned:  "))

    def add_customer(self):
        self.cid = input("Enter Customer ID:  ")
        self.acc_no = input("Enter Account Number:  ")
        self.cname = input("Enter Customer Name:   ")
        self.phone = input("Enter Phone Number: ")
        self.emailid = input("Enter Email ID:   ")
        self.balance = float(input("Enter Balance:  "))
        self.card = input("Enter Card Type: ")


    def display_all(self):
        print("Customer ID:", self.cid)
        print("Account Number:", self.acc_no)
        print("Customer Name:", self.cname)
        print("Phone Number:", self.phone)
        print("Email ID:", self.emailid)
        print("Balance:", self.balance)
        print("Card:", [card.type for card in self.card_owned])

    def card_owned(self, card):
        self.card_used.append(card)
        print(self.name + " owned " + card.card.type)

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0.00

    def add_card(self):
        self.type = input("Enter Card Type: ")
        self.card_no = input("Enter Card Number: ")
        self.cvv = input("Enter Card CVV: ")
        self.expiry_date = input("Enter Expiration Date: ")
        self.balance = float(input("Enter Balance: "))

    def display_card(self):
        print("Card Type:", self.type)
        print("Card Number:", self.card_no)
        print("CVV:", self.cvv)
        print("Expiration Date:", self.expiry_date)
        print("Balance:", self.balance)


c1 = Customer()
c2 = Customer()

cc1 = Card()
cc2 = Card()

c1.add_customer()
c2.add_customer()

cc1.add_card()
cc2.add_card()

c1.debit_from()
c2.credit_to()

cc1.display_card()
cc2.display_card()

c1.display_all()
c2.display_all()