#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# it's like hash map in C
# each pair seperated by ',' and left of the pair is 'key'
#                                right of the pair is 'value'
def main():
    #one way of creating dictionary
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    #other way of creating dictionary and it's more readable
    animals_2 = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr',
        giraffe =  'I am a giraffe!', dragon = 'rawr')
    print_dict(animals)
    print()
    print_dict(animals_2)
    
    #changing a key's value
    print()
    animals_2['lion'] = "i am a lion" 
    print_dict(animals_2),
    
    #adding an elemet
    print()
    animals_2['monkey'] = "lol!"
    print_dict(animals_2)
    
    #using dict methods
    print()
    for k in animals_2.keys():  # in sequence of keys
        print(k)
    print()
    for v in animals_2.values(): #in sequence of values
        print(v)
    print()
    for z,y in animals_2.items(): #in sequene of items
        print("{} says {}".format(z,y))
    print()
    
    print('lion' in animals_2) #returns true or false
    print('found!' if 'lion' in animals_2 else 'nope!') #basic conditional expression with print
    print()
    
    #getting value from the key if key is not exists returns none 
    print(animals_2.get('lion'))
    print(animals_2.get('levy'))
def print_dict(o):
    for x in o: print('{}: {}'.format(x,o[x]))

if __name__ == '__main__': main()
