#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
y = """berker
caner {}""".upper().format(9)
print('x is {} {}'.format(x,y))
print(type(x),type(y))

z = 'berker "{1:<09}" "{0:>010}"'.format(8,1232)
print(z)

a = 8
w = f"it's {a} not {3}"
print(w)

b = 7 * 3.1415 #numeric type
c = 7 / 3
d = 7 // 3
print(type(b), type(c), type(d))


e = 0.1 + 0.1 + 0.1 - 0.3 # makes a problem with dealing money
print(e,type(e))
from decimal import *
a = Decimal('0.1')
b = Decimal('0.3')
e = a + a + a - b
print(e,type(e))

x = (1,'two',3.0,[4, 'four'], 5)
y = (1,'two',3.0,[4, 'four'], 5)
print('x is {}'.format(x))
print(f"type of x {type(x)} id of x {id(x)} id of x[0] {id(x[0])}")
print(f"type of y {type(y)} id of y {id(y)} id of y[0] {id(y[0])}")
#IDs of tuples will be different but id of same elements will be same

if x[0] is y[0]:
    print('yeap')
else:
    print('nope')
    
if type(x) is 'tuple': #CANT USE LIKE THIS
    print('yeap')
else:
    print('nope')

if isinstance(x,tuple):
    print('yeap')
else:
    print('nope')
 
