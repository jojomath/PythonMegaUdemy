# Lists all the build in functions and attributes available
builtIns = dir(__builtins__)
print("====== Built Ins =====")
print(builtIns)

# if you want to know methods or attributes in a particular container try dir(), example below
listMethods = dir(list)
print("====== List =====")
print(listMethods)

# if you want to know what a particukar method does then use help, example
help(list.insert)
help(list.pop)

# script to calculate mean
grades = [ 99, 88, 80, 100 ]
sumOfGrades = sum(grades)
length = len(grades)
mean = sumOfGrades/length
print("Mean grade = ", mean)

# dictionary
dict_grades = {"Mary":90, "Little":95, "Lamb":100}
print(dict_grades)
print(dict_grades.items())
print(dict_grades.keys())
for key in dict_grades:
    print( ">>",key,"got",dict_grades[key],"point out of 100")
    
sumOfGrades = sum(dict_grades.values())
print("Average grade =", sumOfGrades/len(dict_grades))

#Tuples : are immutable while list are mutable
myTuple =  (1,2,2,2,3)
print(myTuple.count(2)) # counts how many times 2 is repeating in the tuple
print(myTuple.index(3)) # returns the first occurance of 3 in the tuple



