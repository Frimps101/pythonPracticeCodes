import re

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo1 = phoneRegex.search("My number is 415-555-4242")
mo1.group()

mo2 = phoneRegex.search("My number is 555-4242")
mo2.group()
