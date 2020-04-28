# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:46:06 2020

@author: Joseph Mathew
"""

# Standard imports
import sys, os, time

# time is implemented in C
# os is implemented in python 
    
print( sys.builtin_module_names )
print( sys.prefix )
print( os.path.exists("VEGetable.txt" ) )
print( os.path.exists("vegetable.txt" ) )

while True:
    if os.path.exists("Vegetable.txt"):
        with open( "Vegetable.txt", 'r' ) as file:
            print( file.read() )
            
    else:
        print( "File does not exist" )
        
    time.sleep(10)