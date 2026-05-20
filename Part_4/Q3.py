class Student:
    def __init__(self,name,roll_no,marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def setter(self,new_name,rollno,new_marks):
        if new_name == "" or rollno < 1 or rollno > 100 or new_marks <= 0:
            print("Please ensure all the details are correct while editing")
        else:
            self.__name = new_name
            self.__roll_no = rollno 
            self.__marks = new_marks

    def getter(self):
        return self.__name,self.__roll_no,self.__marks
    

t1 = Student("Yash",58,99)
# t1.setter("",-5,10)
t1.setter("Raj",10,30)
print(t1.getter())