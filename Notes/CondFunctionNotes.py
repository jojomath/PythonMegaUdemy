# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:17:38 2020

@author: Joseph Mathew
"""

# Conditionals
def mean( value ):
    if type( value ) == list:
        return sum( value ) / len( value )
    elif type( value ) == dict:
        return sum( value.values() )/ len( value )
    else:
        return None
    
def betterMean( value ):
    if isinstance( value, list ):
        return sum( value ) / len( value )
    elif isinstance( value, dict):
        return sum( value.values() )/ len( value )
    else:
        return None
    
print( mean([1,2,3,4,5] ) )
print( betterMean([1,2,3,4,5] ) )

my_dict = {"AA": 1, "BB": 2, "CC": 3, "DD": 4 }
print( mean( my_dict ) ) 
print( betterMean( my_dict ) ) 