# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 07:12:15 2020

@author: Joseph Mathew
"""

# List Comprehension
temps = [221, 234, 340 , 239, -999 ]

# For the puspose of saving memory data ignores decimal points
# divide each value by 10 to get real temperature
actual_temp = [ i / 10  for i in temps  ]
print( actual_temp )

# Ignore -999
actual_temp = [ i / 10  for i in temps if i > -100 ]
print( actual_temp )

# Replace -999 with NaN
actual_temp = [ i / 10  if i != -999 else "NaN" for i in temps ]
print( actual_temp )

# Sum of numbers in a list
def sumOfList( listOfNums ):
    return sum( [ float(val) for val in listOfNums ] )

# New way of formatting
print( "{:.{}f}".format( sumOfList( [ '1.2', 2.1, '3.4' ] ), 2 ) )

# Old way of formatting
print( "%.2f" % sumOfList( [ '1.2', 2.1, '3.4' ] ) ) 