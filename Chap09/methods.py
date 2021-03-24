#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#if first argument is self, it's a method instead of a plane function
class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'
    
    def type(self, t = None): #setter getter
        if t: self._type = t
        return self._type

    def name(self, n = None): #setter getter
        if n: self._name = n
        return self._name

    def sound(self, s = None): #setter getter
        if s: self._sound = s
        return self._sound

    #special method for class
    #it's string representation of the object so when we call print(object) it will print return value of __str__
    
    ''' https://docs.python.org/3/reference/datamodel.html == all the special methods for class'''
    
    def __str__(self): 
        return 'The {} is named "{}" and says "{}".'.format(self.type(),self.name(),self.sound())

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    a0.sound('bark')
    print(a0)
    print(a1)

if __name__ == '__main__': main()
