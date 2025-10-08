class Student:
    def __init__(self):  # constructor function, references itself
        self.stu_id = ""
        self.stu_Name = ""
        self.major = ""
        self.gpa = 0.0
        self.dob = ""
        self.books = []

    def add_student(self):
        self.stu_id = input("Enter Student ID: ")
        self.stu_name = input("Enter Student Name: ")
        self.major = input("Enter Student Major: ")
        self.gpa = float(input("Enter Student GPA: "))
        self.dob = input("Enter Student DOB: ")

    def register_course(self, cc1):
        self.books.append(cc1)

    def edit_student(self):
        self.stu_name = input("Enter Updated Student Name: ")
        self.major = input("Enter Updated Major: ")
        self.gpa = input("Enter Updated GPA: ")
        self.dob = input("Enter Updated DOB: ")


    def display_student(self):
        print("StuID:", self.stu_id)
        print("Student Name:", self.stu_name)
        print("Major:", self.major)
        print("GPA:", self.gpa)
        print("DOB:", self.dob)
        for x in self.courses:
            print("Book Checked-Out: ", x.bookName)


class Book:
    def __init__(self, cid, cname):
        self.bookID = ""
        self.bookName = ""

    def add_book(self):
        self.bookID = input("Enter Book ID: ")
        self.bookName = input("Enter Book Name: ")



s1 = Student()


s1.add_student()
s1.display_student()

b1 = Book("CS1233", "OOP")
b2 = Book("CS2423", "Web APP")
b3 = Book("MTH1163", "Calculas-1")
b4 = Book
b5 = Book

c1.book()     ##  OOP
c2.book()

s1.register_course(c1)
s1.display_student()