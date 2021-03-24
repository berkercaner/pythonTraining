#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ] #list
x[0] = 43
for i in x:
    print('i is {}'.format(i))

print()
y = ( 1, 2, 3, 4, 5 ) #it's a tuple
#y[0] = 43 #cannot reassigned
for i in y:
    print('i is {}'.format(i))

ind = range(5,20,5) # range
for i in ind:
    print(i)
    
x = list(range(5)) #converting to list
print(x)

x={'one': 1, 'two': 2, 'three': 3} ##dict
x['three'] = 42
for k,v in x.items():
    print('k: {}, v: {}'.format(k,v))