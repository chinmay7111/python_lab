def table(n):
    for i in range(1,11):
        yield n*i
        i=i+1
    
for i in table(15):
        print(i)



#  o/p
# -->
# 15
# 30
# 45
# 60
# 75
# 90
# 105
# 120
# 135
# 150
        