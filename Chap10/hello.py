#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a value error')
    except: #as default, occurs in any error
        print('UnknownError: {}'.format(sys.exc_info()[1]))
    else: #if there is no error in try
        print('it\'s okay')
        print(x)        
if __name__ == '__main__': main()
