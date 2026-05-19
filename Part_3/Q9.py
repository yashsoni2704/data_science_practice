list1 = ["apple",9,5.334,"apple",'c',None,5.334,"banana",None]
seen = []
duplicates = []
for ele in list1:
    if ele in seen:
        duplicates.append(ele)
    else:
        seen.append(ele)
print(duplicates)