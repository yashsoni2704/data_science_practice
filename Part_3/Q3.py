list1 = []
for i in range(3):
    n = int(input("Enter Number"))
    list1.append(n)
print("List 1 item collected")
print(list1)
list2 = []
for i in range(3):
    n = int(input("Enter Number"))
    list2.append(n)
print("List 2 item collected")
print(list2)
res = list1 + list2
res.sort()
# res.sort()
print(res)