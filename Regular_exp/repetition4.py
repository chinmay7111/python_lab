import re
str='the supman superman '
supmRegex = re.compile(r'sup(er)+man')
c =supmRegex.search(str)
print(c.group())
# superman

