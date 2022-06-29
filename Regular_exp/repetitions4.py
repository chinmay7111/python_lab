import re
btmRegex = re.compile(r"ba(wo)+an")
c = btmRegex.search("the bawoan movie is good baan and batwoman")
print(c.group())
