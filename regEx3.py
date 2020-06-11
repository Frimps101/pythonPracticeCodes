Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/Frimpomaa/myPythonScripts/regEx2.py ===========
Batman 
Traceback (most recent call last):
  File "C:/Users/Frimpomaa/myPythonScripts/regEx2.py", line 10, in <module>
    print(mo2.group())
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
=========== RESTART: C:/Users/Frimpomaa/myPythonScripts/regEx2.py ===========
Batman 
Batman 
>>> 
=========== RESTART: C:/Users/Frimpomaa/myPythonScripts/regEx2.py ===========
Batman 
Traceback (most recent call last):
  File "C:/Users/Frimpomaa/myPythonScripts/regEx2.py", line 9, in <module>
    print(mo2.group())
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
=========== RESTART: C:/Users/Frimpomaa/myPythonScripts/regEx2.py ===========
Batman 
Traceback (most recent call last):
  File "C:/Users/Frimpomaa/myPythonScripts/regEx2.py", line 8, in <module>
    print(mo2.group())
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
>>> 
>>> import re
>>> heroRegex = re.compile(r'Batman | Tina Fey')
>>> mo2 = heroRegex.search('Tina Fey and Batman')
>>> mo2.group()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mo2.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
=========== RESTART: C:/Users/Frimpomaa/myPythonScripts/regEx2.py ===========
Traceback (most recent call last):
  File "C:/Users/Frimpomaa/myPythonScripts/regEx2.py", line 11, in <module>
    print(mo2.group())
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
=========== RESTART: C:/Users/Frimpomaa/myPythonScripts/regEx2.py ===========
Traceback (most recent call last):
  File "C:/Users/Frimpomaa/myPythonScripts/regEx2.py", line 11, in <module>
    mo2.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
