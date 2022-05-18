#generate password 
import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()"

use_for = lowercase + uppercase + symbols
length_for_pass = 10

password = "".join(random.sample(use_for, length_for_pass))

print("your generated passowrd is: " + password)
