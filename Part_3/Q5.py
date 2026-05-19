dict = {
    "yash":99,
    "raj":50,
    "mohit":70,
    "yoru":45,
    "omen":89
}
print("A = Add a student")
print("B = Update Marks")
print("C = Search for a student")
print("D = Display all students and marks")
    
n = input("Enter Character: ")    
def selection(ch):
    if ch=='A' or ch=='a':
        inputname = input("Enter name of Student: ")
        inputmarks = input("Enter marks of Student: ")
        dict[inputname] = inputmarks
        print(dict)

    elif ch=='B' or ch=='b':
        targetedperson = input("Enter name of student whose marks you want to update")
        if targetedperson in dict:
            updatedmarks = int(input("Enter marks you want to update"))
            dict[targetedperson] = updatedmarks
            print(dict)
        else:
            print("Person not found")
    
    elif ch=='C' or ch=='c':
        targetedperson = input("Enter name of student whom you want to search in database: ")
        if targetedperson in dict:
            result = dict[targetedperson]
            print(f"Name: {targetedperson}, Marks: {result}")
        else:
            print("Student not found")

    elif ch=='D' or ch=='d':
        for name, marks in dict.items():
            print(f"Name: {name} , Marks: {marks}")


    else:
        print("Please select proper operation from the menu")

selection(n)
while True:
    inp = input("Do you want to perform more operation ?: ")
    if inp == "Yes" or inp == "yes":
        n = input("Enter Character: ")    
        selection(n)
    elif inp == "No" or inp == "no":
        print("Ending of program")
        break
    else:
        print("Failed to Select Proper Option")