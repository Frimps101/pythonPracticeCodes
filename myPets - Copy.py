myPets = ['Sophie','Pooka','Fat-tail']
print('Enter a pet name')
name = input()
if name not in myPets:
    print('I do not have a prt named '+ name)
else:
    print(name + ' is my pet') 
