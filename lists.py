"""
List is a collection which is ordered and changeable.-> this allows duplicate members.
Tuple is a collection which is ordered and unchangeable -> this  Allows duplicate members.
Set is a collection which is unordered and unindexed -> this does not duplicate members.
Dictionary is a collection which is unordered, changeable and indexed -> this also does not allow duplicate members.
"""
#handling lists
myList = ["David", "Sun", "Jimmy"]
print(myList)
#The list() Constructor
"""
It is also possible to use the list() constructor to make a list. 
To add an item to the list use append() object method.
 To remove a specific item use the remove() object method.
  The len() function returns the length of the list
"""
constList = list(("Davis", "Brian", "Sun"))
# note the double round-brackets
print(constList)