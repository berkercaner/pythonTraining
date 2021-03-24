#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


import sys
import os
import random
import datetime

def main():
    v = sys.version_info #version of Python
    y = sys.platform #
    
    z = os.name
    t = os.getenv('PATH')
    u = os.getcwd() #current working directory
    r = os.urandom(25) # that returns 25 bytes
    #r = os.urandom(25).hex() => random hex value
    
    a = random.randint(1,1000)
    b = list(range(25))
    random.shuffle(b)
    
    time = datetime.datetime.now()
    
    
    print('Python version {}'.format(v))
    print('Python version {}.{}.{}'.format(*v))
    print("sys.platform: {}".format(y))
    print("os.name: {}".format(z))
    print("os.getenv('PATH'): {}".format(t))
    print("os.getcwd: {}".format(u))
    print("random 25 bytes: {}".format(r))
    print("random.randint(1,1000): {}".format(a))
    print("list b: {}".format(b))
    print("shuffled list b: {}".format(b))
    print(time)
    print(time.year)
    """
    https://docs.python.org/3/library ==>> see all the modules
    """
    
if __name__ == '__main__': main()




