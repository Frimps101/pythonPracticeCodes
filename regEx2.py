import re

"""
heroRegex = re.compile(r'Batman | Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
"""

heroRegex = re.compile(r'Batman | Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

