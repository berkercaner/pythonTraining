#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s.split())
print(s.split('i')) #splits on 'i'

l = s.split() #now its a list

s2 = ':'.join(l) #now s2 is a string
s3 = '|'.join(l)
print(s2)
print(s3)
print("type of l is: {}".format(type(l)))
print("type of s2 is: {}".format(type(s2)))
print("type of s3 is: {}".format(type(s3)))

s4 = "12321_32132_232_38822_3212233_321284_231237_232177_2321321_231239596_543_332_2"
#dashes to spaces
s5 = ' '.join(s4.split("_"))
print(s4)
print(s5)