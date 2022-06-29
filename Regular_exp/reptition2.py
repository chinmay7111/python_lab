import re
btmRegex = re.compile(r"ba(wo)?an")
c = btmRegex.search("the baan movie is good batman and batwoman")
print(c.group())

# baan