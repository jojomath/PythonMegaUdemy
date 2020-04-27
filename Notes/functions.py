# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 06:37:14 2020

@author: Joseph Mathew
"""

def area( a, b = 4 ):
    return a*b

print( "Area of rectangle", area(3) )
print( "Area of rectangle", area( a = 3, b = 5 ) )
print( "Area of rectangle", area( b = 3, a = 5 ) )

a = float( input( "Enter side A of a rect:" ) )
b = float( input( "Enter side B of a rect:" ) )
print( "Area of rectangle", area( a, b ) )



def mean( *args ):
    return sum(args)/len(args)

print( "Mean =", mean( 1, 2,3,4,5,6,7,8,9) )

def keyWordMean(**kwargs):
    return kwargs

print( keyWordMean( a=1,b=2,c=3,d=4 ) )