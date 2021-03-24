#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    x = [1,2,3]  #it's class variable not an object variable
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return 'The {} is named "{}" and says "{}".'.format(self.type(),self.name(),self.sound())

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    
    print(a0)
    print(a1)
    print()
    a1._type = 'levy' #wont change a0.type because _type is object variable (it's not required that change directly, using methods is recommended)
    print(a0)
    print(a1)
    print("-------------------------------")
    
    print(a0)
    print(a1)
    print()
    a0.sound('stop')  #wont change sound variable because _sound is object variable  == encapsulation
    print(a0)
    print(a1)
    
    print("---------------------")
    print(a1.x)
    print(a0.x)
    print()
    a1.x[0] = 7 # it will change both a0.x and a1.x because x is a class variable.
                #dont set variables with _ from outside of the class methods
    print(a1.x)
    print(a0.x)
    
    

if __name__ == '__main__': main()
