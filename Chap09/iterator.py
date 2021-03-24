#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1
        
        #counting number of args
        if numargs < 1:
            raise TypeError('expected at least 1 argument, got {}'.format(numargs))
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else: raise TypeError('expected at least 1 argument, got {}'.format(numargs))

        self._next = self._start
    
    #this iterator method identifies this object as an iterator object
    def __iter__(self):
        return self
    
    #controling the iteration
    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

def main():
    for n in inclusive_range(25):
        print(n, end=' ')
    print()
    for n in inclusive_range(3,38,5):
        print(n, end=' ')
    print()

if __name__ == '__main__': main()
