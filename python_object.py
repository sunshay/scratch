class human:
    def __init__(self, name, age):
    
      self.name= name
      self.age = age
    
    def sayname(self):
        print(self.name, self.age)
        
  
A1 = human("mike", 36)
print(A1.name)
print(A1.age)

class mondial(human):
    pass

A2 = mondial("jules", 20)
A2.sayname()
