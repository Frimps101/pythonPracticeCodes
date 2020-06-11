import re

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world')
beginsWithHello.search('He said hello') == None
