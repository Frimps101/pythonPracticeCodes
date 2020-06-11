import re

phoneNumRegex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
mo = phoneNumRegex.search("My mobile number is 055-640-2727")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group( ))
print(mo.groups())
areaCode,mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
