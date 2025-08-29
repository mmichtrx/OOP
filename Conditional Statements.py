print("Welcome")

a = input("Give me a random number: ")
b = input("Give me a random number: ")
c = input("Give me a random number: ")

if a > b and c < a:
    print("a is the greatest")

elif b > a and b > c:
    print("b is the greatest")

elif c > a and b < c:
    print("c is the greatest")

else:
    print("all the numbers are equal")
