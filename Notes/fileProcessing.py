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

def fileWriteOper( fileName, mode ):
    with open(fileName, mode) as file:
        file.write("\nApple")    
        file.seek(0)
        content = file.read()
        
    print(content)
        
fileWriteOper("Vegetable.txt", mode='a+' )

