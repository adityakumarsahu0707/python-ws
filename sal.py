class employee:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print("Your Name : ", self.name)

class salariedEmployee(employee):
    def __init__(self,name):
        self.name=name
        super().__init__(name)
    def getId(self):
        self.id=input("Enter Your ID = ")
        return("Your Name = ", self.name , " & Your ID = ", self.id)




emp1=employee("Aditya")
emp1.getName()
emp1=emp.getID()
