class Person:
    def __init__(self,nn,dd,gg):
        self.__pname = nn
        self.__dob = dd
        self.__gender = gg

    def display(self):
        print("Person_Name: ", self.__pname)
        print("Person_DOB: ", self.__dob)
        print("Person_Gender: ", self.__gender)
        return ""


class Student(Person):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self, x,y,z)
        self.dept = a
        self.id = b

    def display(self, Value = "", onemore = ""):
        print(Person.display(self))
        print("Stu_Dept: ", self.dept)
        print("Stu_ID: ", self.id)
        if Value != "":
            print("Within Polymorphism", Value)

class Faculty(Person):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self, x,y,z)
        self.dept = a
        self.desig = b

    def display(self):
        print(Person.display(self))
        print("Fac_Dept: ", self.dept)
        print("Fac_Design: ", self.desig)

s1 = Student("Michael", "2007", "Male", "IS", "123")
s1.display()

f1 = Faculty("Joe", "1997", "Male", "Bible", "Professor")
f1.display()