# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:56:56 2020

@author: Joseph Mathew
"""

my_dict = {"Name": "Joseph", "Age": 30, "Sex": 'M', "Income": 999.9, "Country": 'CA' }
print(my_dict)

# Cannot index dict like lists
print(my_dict["Name"])

keys = my_dict.keys();
items = my_dict.items();
print("Keys:", keys)
print("Items:", items)

print("\n==== Start of Dict Values ===")
for key in my_dict:
    print(key, ":", my_dict[key])
print("==== End of Dict Values ===")