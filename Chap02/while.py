#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

n = 0
while(n < 5):
    print(words[n])
    n += 1

while 1:
    try:
        val = int(input("Enter pass: "))
        if val == 321332:
            print('successful')
            break
        print("try again")
        
    except:
        print("not a valid number")