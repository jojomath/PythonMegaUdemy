# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:02:56 2020

@author: Joseph Mathew
"""

# Mean function for a list, this is not defined by default by Puthon
def mean( myList ):
    sumOfList = sum( myList )
    numOfItems = len( myList )
    meanOfList = sumOfList/numOfItems
    
    return meanOfList


list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

print( list1 )
print( "Mean:", mean( list1 ) )

print( "Builtin:\t", type( sum ) )
print( "Newly defined:\t", type( mean ) )
print( "List:\t\t", type( list1 ) )
