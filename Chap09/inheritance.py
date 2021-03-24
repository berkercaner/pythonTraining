#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

class Duck(Animal): #inheriting
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)      #super classs the parent class

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)
        
    def kill(self,s):
        print("{} will now kill all {}".format(self.name(),s))

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(),o.name(),o.sound()))

def main():
    a0 = Kitten(name = 'fluffy', sound = 'rwar')
    a1 = Duck(name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans') #this wont work for Duck because it's only defined in kitten child class

if __name__ == '__main__': main()
