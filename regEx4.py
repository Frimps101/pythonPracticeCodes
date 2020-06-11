import re

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
a = mo.group(1)
print(a)
