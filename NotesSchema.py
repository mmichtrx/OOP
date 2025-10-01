class Student:
    def _init_(self):  # constructor function, references itself
        self.stu_id = ""
        self.stu_Name = ""
        self.major = ""
        self.gpa = 0.0
        self.dob = ""

    def add_student(self):
        self.stu_id = input("Enter Student ID: ")
        self.stu_name = input("Enter Student Name: ")
        self.major = input("Enter Student Major: ")
        self.gpa = float(input("Enter Student GPA: "))
        self.dob = input("Enter Student DOB: ")

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

#Main Code

s1 = Student()          #creates A object, it calls the constructor function

s1.add_student()
s1.display_student()


s2 = Student()          #creating new students
s3 = Student()
s3.display_student()        #the s is to show which student it is i.e: student1 student2 student3: s1 s2 s3

myList.append()

course1 = Courses()     #both to add courses
course1.add_course()

s1.add_course()     #invalid way to add courses
course1.add_student()   #invalid also
mylist.update()     #invalid cross-calling due to list
mylist.append()     #invalid cross-calling due to dictionary


