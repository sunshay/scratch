#!usr/bin/python3

a = 'fred'
#b = str(40)
b = 40
#weather = "\tIt's kind of sunny,\nhope we have a good day!"

message = "Hello, My name is {} and I'm {} years old.".format('fred', 40)
print(message)
#print('I am ' + a + " my age is "+ b) #b is a integer but we add str to enforce print 
#print(f'I am {}') #this is the printf-style formatting to avoid "+" signe
#print(weather)

class test():
    def __init__(self,fname,lname,age,session):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.session = session

    def introduce(self):
        print("My name is " + self.firstname)
        print("I am " + str(self.age) )

person = test('Mike', 'Mawezi',35, 2022 )
person.introduce() #a method introduce called in test class 