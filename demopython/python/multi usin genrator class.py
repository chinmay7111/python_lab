def multi_yield():
    str1="first string"
    yield str1

    str2='second string'
    yield str2

    str3='third string'
    yield str3

obj = multi_yield()
print(next(obj))
print(next(obj))
print(next(obj))



# PS E:\Chinmay\demopython> python -u "e:\Chinmay\demopython\python\multi usin genrator class.py"
# first string
# second string
# third string