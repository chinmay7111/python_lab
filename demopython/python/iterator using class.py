class MyNumbers:
    def __iter__ (self):
        self.a=1
        return self
    def __next__ (self):
        x=self.a
        self.a+=1
        return x
myclass = MyNumbers()
miter = iter(myclass)
print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter))
print(next(miter))

# o/p->
# 1
# 2
# 3
# 4
# 5



