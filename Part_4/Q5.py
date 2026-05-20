# 2 class using the same parent class example

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)
#         self.seats = seats

# class Bike(Vehicle):
#     def __init__(self,brand,model,engine_CC):
#         super().__init__(brand, model)
#         self.engine_CC = engine_CC
# B1 = Bike("Yamaha",2026,"150CC")
# C1 = Car("BMW",2026,4)
# # print(B1.brand,B1.model,B1.engine_CC)
# print(C1.brand,C1.model,C1.seats)




#Mutilple Inheritance

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class Car:
#     def __init__(self,seats):
#         self.seats = seats

# class Bike(Vehicle,Car):
#     def __init__(self,brand,model,seats,engine_CC):
#         super().__init__(brand, model)
#         Car.__init__(self,seats)
#         self.engine_CC = engine_CC

# B1 = Bike("Yamaha",2026,3,"150CC")
# # C1 = Car("BMW",2026,4)
# print(B1.brand,B1.model,B1.seats,B1.engine_CC)
# # print(C1.brand,C1.model,C1.seats)


#Multilevel Inheritance
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)
#         self.seats = seats

# class Bike(Car):
#     def __init__(self,brand,model,seats,engine_CC):
#         super().__init__(brand, model,seats)
#         self.engine_CC = engine_CC

# B1 = Bike("Yamaha",2026,3,"150CC")
# C1 = Car("BMW",2026,4)
# print(B1.brand,B1.model,B1.seats,B1.engine_CC)
# print(C1.brand,C1.model,C1.seats)