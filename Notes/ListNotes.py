# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:42:39 2020

@author: Joseph Mathew
"""

myList = [ 1, 2, 2, 3, 2, 2, 2, 3 ]
print("Original List:", myList)

myList.append(4) #append
print("After append:", myList)

# Indexing, btw Python is zero indexing
print("First index of 1:", myList.index(1))
print("First index of 2:", myList.index(2))
print("First index of 3 starting from index 3:", myList.index(3, 3))
myList.remove(2)
print("After removing 2:", myList) # removes the first match it finds
myList.pop()  #removes last item from the list
print("After pop:", myList)
