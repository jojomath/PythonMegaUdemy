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

# Get Item given index
print("Item at index 1:", myList.__getitem__(1)) # do not use this method, it's supposed to be internal
print("Item at index 1:", myList[1]) # instead use this


#Slicing a list
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
print(list1[1:4]) # 1 is included but 4 is not
print(list1[:4]) # index 0 is included but 4 is not
print(list1[4:]) # index 4 and above

# Negative indexing
print("Last item:",list1[-1]) # last index
print("Last 2 items:", list1[-2:])
print(list1[-5:-2]) # starts fron -5 index and -2 index is not included


# Note: indexing works for Strings as well