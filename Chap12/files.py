#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt') #by default it's read only
    """ 
         f = open('lines.txt', 'w') ==>open it in wright mode, it will empty the file if opened in wright mode
         f = open('lines.txt', 'a') ==>open it in append mode, it will start writing from the end of the file
         f = open('lines.txt', 'r+t') ==> text mode
         f = open('lines.txt', 'r+b') ==> binary mode
    """
    for line in f:  #file object is an iterator
        print(line.rstrip()) #each of the line is a string so we can use string methods
                             #rstrip() method avoids white spaces right side of the each line

if __name__ == '__main__': main()
"""
    strings might work differently for different system
    for different system line ending might be different
    for example x = "levy"
    ==> some systems(unix based systems, modern Mac) -> "levyLF" = 5 bytes string 
    LF=line feed character ASCII 10 decimal or 0A hex
    ==> some systems(older systems: apple II, classic Mac, TRS-80, old commadore systems) -> "levyCR" = 5 bytes string
    CR = carrige return character ASCII 13 decimal or 0D hex 
    ==> some systems(other older systems CP/M, OS/2,) -> "levyCRLF" = 6 bytes string
    
    !!because of the need to properly recognize any comination of these line endings most systems have different modes
    for opening text files and non text or binary files
"""