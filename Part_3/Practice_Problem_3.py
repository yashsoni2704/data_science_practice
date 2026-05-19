info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

# 1: Create a dictionary where the keys are student names and the values are sets of courses they are enrolled in.
dict = {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)


# 2: Create a set of all unique courses that students are enrolled in.
# unique_course = set()
# for val in info:
#     unique_course.add(val[1])
# print(unique_course)

    
# 3: Create a list of all students enrolled in "English".
# for name,subject in info:
#     # print(subject)
#     if(subject == "English"):
#         print(name)

