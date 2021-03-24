

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
    https://docs.python.org/3/library/stdtypes.html ==> every string methods 
"""

#we can create our own string class 
#str is built in
class MyString(str):
    def __str__(self):
        return self[::-1] #returns backwards

print('Hello, World.')
print(MyString('Hello, World.'))

print("-----------------------------------------------------")

""" string methods:
    upper() all letters uppercase
    lower() all letters lowercase
    capitalize() only first letters
    title() first letter of everyword
    casefold() every letter like ß will be lowercase
    """
#strings are immutable, strings cannot be changed
#these methods create different object
s1 = "levy"
s2 = s1.upper() #this method isn't just transforming string, creating an another object
print(id(s1))
print(id(s2))

print(s1 + ' ' +s2)

print("-------------------------------------------------------")

x = 13
y = 49

print('the number is {0} {1} {0}'.format(x,y))

print('the number is {0:<05} {1:>+0}'.format(x,y))

z =  x*y*y*1000 
print('the number is {:,}'.format(z)) #comma for thousand seperation
# = 31213000 ==> 31,213,000 with {:,}
print('the number is {:,}'.format(z).replace(',','.'))

print('the number is {:x}'.format(z)) #hexadecimal












