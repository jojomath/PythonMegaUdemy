# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:56:28 2020

@author: Joseph Mathew
"""

mon_temp = [ 1.2, 2.3, 3.4, 4.5, 5.6 ]

for temp in mon_temp:
    print( round( temp ) )
    
for letter in 'Hello':
    print( letter.upper() )
    
my_dict = {"Mary": 25, "Joan": 28, "Barry": 10 }

for items in my_dict.items():
    print( items )
    
for key in my_dict.keys():
    print(key, ":", my_dict[key] )
    
for value in my_dict.values():
    print( value )