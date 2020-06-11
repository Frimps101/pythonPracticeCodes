import requests

r=requests.get('https://xkcd.com/353/')
#print(r.text)
#print(r.content)

#r = requests.get('https://imgs.xkcd.com/comics/python.png')

#This is just writing the contents of r.content into a file
#with open('comic.png','wb') as f:
#    f.write(r.content)

#Checking your responses using status_codes
print(r.status_code)
print(r.ok)
print(r.headers)
