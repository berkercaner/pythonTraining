#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = x+y
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 2')
    print('line 3')
print('line 4') #incorrect indentation

print('z is {}'.format(z))
print('last line')
