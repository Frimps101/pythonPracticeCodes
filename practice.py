import re
"""
pattern = re.compile("Bat(man|mobile|woman|car)")
string_to_check = pattern.search("I think Tina Fey can be Batwoman if she wants")
print(string_to_check.group())

pattern = re.compile(r"Batman|Tina Fey")
search_string = pattern.search("I heard Batman and Batwoman were dating")
print(search_string.group())

pattern = re.compile(r"Bat(wo)?man")
search_string = pattern.search("I heard  Batwoman were dating")
print(search_string.group())

pattern = re.compile(r"Bat(wo)*man")
search_string = pattern.search("I heard  Batwowowowoman were dating")
print(search_string.group())

pattern = re.compile(r"Bat(wo)+man")
search_string = pattern.search("I heard  Batwoman were dating")
print(search_string.group())

pattern = re.compile(r'(Ha){3}')
search_string = pattern.search("He told a joke and i laughed HaHaHa")
print(search_string.group())

pattern = re.compile(r'(ha){2,5}?')
search_string = pattern.search("He told a joke and i laughed haha")
print(search_string.group())

pattern = re.compile(r"\d{4}-\d{3}-\d{3}")
search_text = pattern.findall("My mom's number is 0540-752-055 and my aunt's number is 0242-660-835")
print(search_text)

pattern = re.compile(r"\d+\s\w+")
search_text = pattern.findall("12 drummers, 11 pipers, 10 lords")
print(search_text)

pattern = re.compile(r"[aeiouAEIOU]")
search_text = pattern.findall("Dont talk too much let your body talk")

pattern = re.compile(r"[0-5]")
text = pattern.findall("He thought i was kidding about his brother being unable to count from 1 2 3 4 5")
print(text)

pattern = re.compile(r"[^aeiou]")
text = pattern.findall("Robocop eats babyfood")
print(text)

pattern = re.compile(r"^Hello")
text = pattern.findall("Hello world")
print(text)
"""

pattern = re.compile("^Hello")
beginsWithHello = pattern.search("he said hello")
print(beginsWithHello == None)







