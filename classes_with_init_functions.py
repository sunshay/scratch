"""
init function adds more values to our python function values...
"""

#consider the following example, using python with init...
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Sunshayina", 33)

print(p1.name)
print(p1.age)