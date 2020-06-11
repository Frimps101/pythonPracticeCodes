catNames = []
while True:
    print("Enter name of cat " + str(len(catNames) + 1) + " Or enter nothing to stop.):")
    name = input()
    if name == "":
          break
    catNames.append(name)
    #catNames = catNames + [name]

    
print("The cat names are: ")
for name in catNames:
          print(" "+ name)
    
