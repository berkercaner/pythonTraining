#all functions return a value


def main():
    '''kitten(5)   
    x = kitten(3)
    print(x) # will print None
    y = cat(1)
    print(y)'''
    x = [15]  # it's an integer and at the same time it's a one element list so we can say x[0]
    print(x)
    wontChange(x) #wont change because function wontChange uses copy of the x => call by value
    print(x)
    willChange(x) #will change because function willChange uses reference of the x
    print(x)
    """
    with the same way if we make mutual 2 lists together same thing will happen
    """
    print("------------------")
    a = [3,2,1]
    b = [3,2,1]
    print("a: {}\nb: {}".format(a,b))
    a = b
    b[0] = 99 # will change a[0] too
    print("a: {}\nb: {}".format(a,b))
def willChange(y):
    y[0] = 3  #call by reference

def wontChange(z):
    z = 3     #call by value

def kitten(n):
    print('{} meow'.format(n))

def cat(m):
    return '{} meow'.format(m)

if __name__ == '__main__': main()