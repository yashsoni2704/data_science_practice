class A:
    def __init__(self,name):
        self.name = name

class B:
    def __init__(self,age):
        self.age = age

class C:
    def __init__(self,address):
        self.address = address

class D(A,B,C):
    def __init__(self,name,age,address,gender):
        super().__init__(name)
        B.__init__(self,age)
        C.__init__(self,address)
        self.gender = gender

t1 = D("Yash",22,"No Home","Male")
print(t1.name,t1.age,t1.address,t1.gender)