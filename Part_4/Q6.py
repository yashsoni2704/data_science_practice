from abc import ABC, abstractmethod

class Salary(ABC):
    @abstractmethod
    def print_salary(self):
        pass

class TA(Salary):
    def print_salary(self):
        print(15000)

class FullTimeEmployee(Salary):
    def print_salary(self):
        print(50000)

t1 = FullTimeEmployee()
t1.print_salary()
t2 = TA()
t2.print_salary()