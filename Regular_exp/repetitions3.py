import re 
str1='the superman is very powerful superwoman and superman movie is good'
str2='the superwoman is very powerful superwoman and superman movie is good'
supmRegex= re.compile(r'super(wo)*man')
c = supmRegex.search(str1)
h = supmRegex.search(str2)
print(c.group())
print(h.group())

# superman
# superwoman
