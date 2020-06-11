import requests

#Creating a dic of the parameters
#payload = {'page':2,'count':25}

#r = requests.get('https://httpbin.org/get', params=payload)
#print(r.text)
#print(r.url)

#payload = {'username':'Jo','password':'testing'}
#r = requests.post('https://httpbin.org/post', data=payload)
#print(r.text)
#print(r.url)
#print(r.json())
#r_dict = r.json()
#print(r_dict['form'])

#Passing credentials for basic authentication
#You just have to pass in some additional parameters ie auth
#We pass a tuple to the auth which will contain the username and password
#r = requests.get('http://httpbin.org/basic-auth/jo/testing', auth=('jo','testing'))
#print(r.text) 

r = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r)