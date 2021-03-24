#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x) #int is a consructor for an int type, it's not a function
z = abs(-y)
t = divmod(y,5) #returns a tuple with mode 47/5 = 9*5+2 => (9,2)
u = 13 +4j 
v = complex(13,4)


print('x is {}'.format(type(x)))
print('x is {}'.format(x))

print('y is {}'.format(type(y)))
print('y is {}'.format(y))

print('z is {}'.format(type(z)))
print('z is {}'.format(z))

print('t is {}'.format(type(t)))
print('t is {}'.format(t))

print('u is {}'.format(type(u)))
print('u is {}'.format(u))

print('v is {}'.format(type(v)))
print('v is {}'.format(v))
