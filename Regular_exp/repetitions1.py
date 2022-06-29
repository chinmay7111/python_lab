import re
haRegex = re.compile(r'(😀){2,5}')
mo1= haRegex.search('hahahaha 😀😀😀  ')
print(mo1.group())

# 😀😀😀