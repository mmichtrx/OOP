class Vehicle:
    def __init__(self, mm, mm2, vt):
        self.__vmake = mm
        self.__vmodel = mm2
        self.__vtype = vt

    def display(self):
        print("Vehicle_Make: ", self.__vmake)
        print("Vehicle_Model: ", self.__vmodel)
        print("Vehicle_Type: ", self.__vtyp)
        return ""

class Car(Vehicle):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self, x,y,z)
        self.ccr = a
        self.cid = b

        def display(self):






v1 = Vehicle()
v1.display()