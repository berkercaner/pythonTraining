#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if y in x:
    print('expression is true')
else:
    print('expression is false')

if y is x[0]:  #because they have same ID
    print('expression is true')
else:
    print('expression is false')
    
if y is not x[1]:  
    print('expression is true')
else:
    print('expression is false')