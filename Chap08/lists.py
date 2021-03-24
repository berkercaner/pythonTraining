#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    
    i = game.index('Lizard')
    print("Lizard's index : {}".format(i))
    print("original: ")
    print_list(game)
    game.append('levy') #append to the end
    print("appended 'levy':")
    print_list(game)
    print("inserted 'malloc' to index 5:")
    game.insert(5,'malloc')  #inserting into index
    print_list(game)
    print("1:5 index printed: ")
    print(game[1:5])
    
    print()
    
    print("The element 'Rock' is removed: ")
    game.remove('Rock') #removing by value
    print_list(game)
    print(game)
    print()
    
    x = game
    print("x = list and x is printed: ")
    print(x)
    print("x= game.pop() and x is printed:")
    x = game.pop() #removing end of the list ''stack simulation''
    print(x)
    print("list is printed after x = game.pop():")
    print(game)
    
    print("list is printed with print(','.join(game):")
    print(', '.join(game))
    print("list's length:")
    print((len(game)))
    
    gameT = ('Rock', 'Paper', 'Scissors') #it's tuple same as list but not mutable      
                                          # cant append remove insert
    print("its a tuple")
    print(gameT)
 
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
