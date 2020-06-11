class Person:
        def __init__(self,firstname,lastname,school):
                self.firstname = firstname
                self.lastname = lastname
                self.school = school
        def myFunc(self):
                print(firstname, lastname)

                
class Student(Person):
        def __init__(self,fname,lname,year):
                super().__init__(fname,lname)
                self.graduationYear = year
        def welcome(self):
            print("Welcome ", self.firstname,self.lastname," to the class of ",self.graduationYear)




s1 = Student("Max","Kwakye",2022)
#s1.welcome()

p1 = Person("Josephine","Kwakye","University of Ghana")
p1.firstname


