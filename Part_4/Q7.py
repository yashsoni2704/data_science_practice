class construtor_Overloading:
    def __init__(self,name,age=None,address=None):
        self.name = name
        self.age = age
        self.address = address

t1 = construtor_Overloading("Yash")
t2 = construtor_Overloading("raj",19)
t3 = construtor_Overloading("Mohit",24,"No Home")
print(t1.name)
print(t2.name,t2.age)
print(t3.name,t3.age,t3.address)