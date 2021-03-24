#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class hoop:
    def __init__(self,n):
        self._n = n 
    def __repr__(self):        ## WITHOUT THIS LINE THE "repr" function returns an adress
        return 'repr-> {}'.format(self._n)
    def __str__(self):
        return 'str-> {}'.format(self._n)

s = 'hello Levy'
print(repr(s))

print()

x = hoop('hello levvy s2')
print(repr(x)) #if we specify like repr() this will print the returned value of __repr__ function in the class
print(x) #if we don't this will print the returned value of __str__ function
"""
    without __str__ method in the class, print(x) and print(repr(x)) both print __repr__ method's return value
    and without both of these __str__ and __repr__ print(x) and print(repr(x)) will print the adress of the value
    
"""
print(chr(128406))# return characters of a number 
print(ord('🖖')) #  returns number of a character 🖖 ==> it's a unicode character 
print(chr(128433))
"""
    https://docs.python.org/3/library/functions.html  ==> all built in functions
"""

print("-----------------------------------------------------------")

a = (1,2,3,4,0)
b = reversed(a) #returns an adress
c = list(reversed(a)) #returns a reversed list
d = [None]*5
d[0] = sum(c)
d[1] = any(c)#if any element is different than 0 it returns true
d[2] = all(c)#if all of them are true, returns true
d[3] = min(c)
d[4] = max(c)
print(a)
print(b)
print(c)
print(d)
print("-------------------------------")
e = (1,2,3,4,0)
f = (4,5,10,2,1)
g = zip(e,f) #it zips these tuples together but works differently
for l,m in g: print("l: {} - m: {}".format(l,m))
print()
w = ('cat','dog','rabbit','cheetah','lion')
for j,k in enumerate(w): print("{}: {}".format(j,k))










