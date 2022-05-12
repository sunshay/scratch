#!/usr/bin/python

filename = "variable.py"
text = open(filename).read()
text = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
open(filename, "w").write(text)
#The problem is the code uses curly quote characters (“” and ''), but Python only supports straight quote characters ("" and ''). 