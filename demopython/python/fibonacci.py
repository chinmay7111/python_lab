last = 6
a=0
b=5

print(a, end = " ")
print(b, end = " ")

for i in range (2, last+1):
    c = a+b
    a = b
    b = c   
    print(c, end =" ")

    # o/p-->0 5 5 10 15 25 40