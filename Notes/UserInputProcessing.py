# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:41:04 2020

@author: Joseph Mathew
"""

#User Input Processing

abc = input("Enter Temperature: ")
print(abc)
print(abc, "is of type:", type(abc))

tempInTemp = float(abc)
print( tempInTemp, "is of type", type( tempInTemp ))

# Multiple variables are provided as tuple
msg = "%.2f is type of %s" % (tempInTemp, type(tempInTemp))
print(msg)

# f-string is really an expression evaluated at run time, not a constant value.
msg = f"{tempInTemp} is type of {type(tempInTemp)}"
print(msg)