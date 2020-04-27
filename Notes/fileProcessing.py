# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 07:13:36 2020

@author: Joseph Mathew
"""

def fileReadOper( fileName ):
    file = open(fileName)
    content = file.read()
    file.close()
    
    return content

def fileReadOper2( fileName ):
    with open(fileName) as file:
        content = file.read()    
    return content

def fileWriteOper( fileName, mode='a' ):
    with open(fileName) as file:
        file.write("Apple")    
        
        
fileWriteOper("Vegetable.txt" )