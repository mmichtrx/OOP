stu_name = input("Enter Student Name:")

course1 = int(input("Enter the grade for Course1:") )
course2 = int(input("Enter the grade for Course2:") )
course3 = int(input("Enter the grade for Course3:") )
course4 = int(input("Enter the grade for Course4:") )
course5 = int(input("Enter the grade for Course5:") )

total = course1 + course2 + course3 + course4 + course5
print("Your total is", total)

avg = total/5

print("Your average is:", avg)