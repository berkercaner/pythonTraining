#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt') #it's default rt but better to specify
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        #outfile.writelines(line) ==> it'll work the same way but print function dealing line endings by default.
        #so print is more useful
        print('.', end='', flush=True) #for make a little progress bar #flush is flushes the output buffer
                                       #end='' is for printing in same line, not to the next line
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()
