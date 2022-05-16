#write a program that makes a string containing the names of all the students in a class that begin with "S"
name = ["sam","saly", "Adam","Paulina"]
s_name = ""

for n in names:
    if n.start("s"):
        s_name = s_name + n + ""

print("The students whose names begin with 'S' are: " + s_names)
