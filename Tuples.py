#!python3
# Revision of tuples from think python3


'''
t1 = ('a',)
print(type(t1))

t = ('lupins')
print(tuple(t))

l1 = ['cat','dogs','cows']
print(tuple(l1))

l2 = tuple()
for i in range(10):
    l2 = i
    print(l2)

tupleSomething = (1,2,3,4,5)
tupleSomething = ('A',) +tupleSomething[1:]
print(tupleSomething)

#string eg
greeting = 'Vella Ciao'
greeting = ('B') + greeting[1:]
print(greeting)

print((1,2,3,3) > (4,5,6,7))
print((1,2,3,3) < (4,5,6,7))

#Tuple Assignment
a=10
b=50
c=30

a,b,c = c,a,b
print("a: ",a , "b: ",b , "c: ",c)

cat,dog,anotherDog = ["Pussy","Wonder","Small"]
print(cat)
print(dog)
print(anotherDog)

#Splitting an email into a username and a domain

myEmail = "jkwakye001@gmail.com"
userName,domain = myEmail.split("a")
print("UserName is: " + userName)
print("Domain is: " + domain)

quot,rem = divmod(7,3)
print(quot)
print(rem)

def min_max(t):
    return min(t),max(t)


t = (30,24,5,28,10)
print(min_max(t))

total = 0
t = (23,4,5,6,7,2,3,1)
for i in t:
    total += i

print(total)

def doAll(*args):
    print(min(args))
    print(max(args))
    print(sum(args))



print(doAll(21,24,24,13,94))

s = 'josephine'
t = 'frimpomaa'
u = 'kwakye'

for j in zip(s,t,u):
    print(j)


list1 = ('Benjamin','Joseph','Mary')
list2 = ('Jenji','Josephine','Martha')

for f, l in zip(list1,list2):
    print(f,l)

for index,value in enumerate('abcd'):
    print(index,value

participant = {"Jo":"Adidas","Nana":"Nike","Bro Lawlaw":"Puma"}
print(participant.items())

t = [('cats',0),('dogs',1),('cows','3')]
j = dict(t)
print(j)
'''
d = dict(zip('abc',range(3)))
print(d)
