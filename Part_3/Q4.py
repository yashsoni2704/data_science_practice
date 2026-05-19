tup = (1,4,3,2,5,7,9,3)
tup_even = ()
tup_odd = ()
for n in tup:
    if n%2==0:
        tup_even = tup_even + (n,)
    else:
        tup_odd = tup_odd + (n,)
print(tup_odd)
print(tup_even)