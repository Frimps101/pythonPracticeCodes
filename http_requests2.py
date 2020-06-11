import requests


r = requests.get('https://imgs.xkcd.com/comics/python.png')

writeText = open('getRequests.txt')
writeText.write(r.text)

