# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:57:29 2020

@author: Joseph Mathew
"""
#Variable Updating
a = 2
a = 4
a = 6
print( a + a + a) # 18 is expected

#Type Error
a = "1"
b = 2
print( int(a) + b )

#Sequence Indexing
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print( letters[1] )

#Slicing
print( letters[3:6] )
print( letters[:3] )

#Negative Indexing
print( letters[-2] )
print( letters[-3:] )

#Step Slicing
res = []
for val in letters:
    if letters.index(val) % 2 == 0:
        res.append(val)
        
print( res )
#easier way
print
print( letters[::2] )
print( letters[1::2] )