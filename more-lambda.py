"""
lambda is mainly used when working with more of numbers which values we don't have...
"""

#using lambda with functions....
def lambda_function(x):
    #where, we don't know the value of x...
    return lambda a : a * x
# multiply the function...
y = lambda_function(4)
print y(2)