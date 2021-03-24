#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    seq2 = [x for x in seq if x % 3 != 0] #all the elements in seq that are not divived by 3
    seq3 = [x * 2 for x in seq]
    seq4 = [(x, x**2) for x in seq] #list of tuples
    from math import pi
    seq5 = [round(pi,i) for i in seq] #rounding pi
    seq6 = {x: x**2 for x in seq} #creating dict
    seq7 = {x for x in 'superduper' if x not in 'pd'} #creating a set without p and d letters
    
    print_list(seq) #instead of wright for i in seq print(i)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6) #our function not gonna work because it's a dict now.
    print(seq7)
def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
