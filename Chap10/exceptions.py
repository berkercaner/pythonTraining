#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    """raise command triggers the specific exception that follows with the
    specific error message"""
    if numargs < 1:
        raise TypeError('expected at least 1 argument, got {}'.format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

def main():
    try:
        for i in inclusive_range():
            print(i, end = ' ', flush = True)
        print()
    except TypeError as e:
        print('Range error: {}'.format(e))
if __name__ == '__main__': main()
