file1 = open("test1.txt", "w")

file1.writelines("Hello World!")
file1.writelines("Welcome teo OOP class!")
file1.writelines("Have a good time!")

file1.close()

file2 = open("test.txt", "r")
for line in file2:          #line is a variable you could make it anything x, a, b etc
    print(line)

file2.close()