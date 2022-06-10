import re
from traceback import print_tb


def fun():
    print("helloo")
fun()

def is_prime(n):
    if n in [2,3]:
        return True
    if n % 2 == 0:
        return False
    r =3
    while r*r<=n:
        if n%r ==0:
            return False
        r +=2
    return True
print(is_prime(76), is_prime(74))   


# PS E:\Chinmay\demopython> python -u "e:\Chinmay\demopython\test_range.py"
# helloo
# False False