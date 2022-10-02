"""
Python is an Object Oriented Programming language that everything is done under objects and methods in a class.
"""
from dataclasses import dataclass, field
import random
import string

# class Bicycle:
#     def __init__(self, size: int, weight: int, model: str, active: bool = True):
#         self.size= size
#         self.weight = weight
#         self.model = model
#         self.active = active
    
    # def __str__(self):
    #     return f"{self.size},{self.weight},{self.model}"
    
@dataclass 
class Bicycle:
    size: int
    weight: int
    model: str
    # active: bool = True
    # email: list[str] = field(default_factory=list)
    # id: str 
  
r=Bicycle(5,28,"mountain")
print(r)
