#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
It's a collection type. contains unordered collection of unique
and immutable objects
"""
def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Levy. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
