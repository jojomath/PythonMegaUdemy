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