first = []
second = []
for i in range(5):
    n = int(input("1st: "))
    first.append(n)
for i in range(5):
    n2 = int(input("2nd: "))
    second.append(n2)
print(first,second)
set1 = set(first)
set2 = set(second)
print(set1.union(set2))
print(set1.intersection(set2))