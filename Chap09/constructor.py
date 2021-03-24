#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # "__init__" is a special name for class consructor
    # first argument is always self and that's what makes it a method because self points to the object
    #next 3 arguments are used to initialized the object variables
    def __init__(self, type, name, sound):
        #these are object variables because they don't exist in class
        #without having been consructed into an object || until after the object is defined
        #object variables defined with '_type' => it's traditional
        #in order to access these object variables, we use getters
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

"""
===>because of the when the time that didnt remember the argument order, we could use like this=>
    class Animal:
    def __init__(self,**kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']
    
===>and when we call the consructor, call like this =>
    something = Animal(type='kitten', name='fluffy', sound='rwar') ==> it will do the samething but more safely
                                                                   ==> we can put them any order
===>we can give a default value if an argument missing
    def __init__(self,**kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'
    
"""

def print_animal(o): 
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
