stu_name = input("Enter Student Name: ")

course1 = int(input("Enter the grade for Course1: ") )
course2 = int(input("Enter the grade for Course2: ") )
course3 = int(input("Enter the grade for Course3: ") )
course4 = int(input("Enter the grade for Course4: ") )
course5 = int(input("Enter the grade for Course5: ") )

total = course1 + course2 + course3 + course4 + course5
total_percentage = ((total/500)*100)
print("Your total is", total)

avg = total/5

print("Your average is:", avg)

if total_percentage < 100 and total_percentage > 90:
    print("Grade A")
elif total_percentage < 89 and total_percentage > 80:
    print("Grade B")
elif total_percentage < 79 and total_percentage > 70:
    print("Grade C")
elif total_percentage < 69 and total_percentage > 60:
    print("Grade D")
elif total_percentage < 59 and total_percentage > 0:
    print("Grade F")