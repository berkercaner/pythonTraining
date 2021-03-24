#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'
    step = 0

    def quack(self): #self is reference to the object ==> can be named of anything but 'self' is traditional
        print(self.sound)

    def move(self):
        print(self.movement)
    
    def increaseStep(self):
        self.step += 1
    
    def getStep(self):
        return self.step

def main():
    donald = Duck()
    print(donald.sound) #same as using with methods but using methods is more recommended 
    donald.quack()
    donald.move()
    
    x = donald.getStep()
    print("Before increasing with method step = {}".format(x))
    
    
    
    for i in range(5):
        donald.increaseStep()
    
    x = donald.getStep()
    print("After increasing with method step = {}".format(x))

if __name__ == '__main__': main()
