import re

batRegex = re.compile(r"Bat(wo)?man")
print(batRegex.search("I love batwoman").group())

