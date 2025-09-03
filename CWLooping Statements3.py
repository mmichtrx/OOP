p = int(input("Enter principal loan amount: "))
R = int(input("Enter rate of interest: "))
n = int(input("Enter duration of the loan: "))

r = R / (12*100)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)
for i in range(1,n):
    print(p-emi)
    balance = p-emi
    print(balance)
    p = balance