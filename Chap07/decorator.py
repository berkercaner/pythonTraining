

def func():      # in python everything is an object so functions are type of object
    print('this is func')
    
x = func  #function can be assinged like function pointers in C
x()

def func1():
    def func2():
        print('this is func2')
    return func2 #func1 returns func2
    
y = func1()
y()
#'func2()'' #it causes an error 'not defined' cant be called because it's declared in func2

def func3():
    print('this is func3')
    
print('\n\n')
##############################3
def f1(inputF): #decorator function
    def f2(): #
        print('before the function call')
        inputF()
        print('after the function  call')
    return f2
    
@f1 #decorator
def f3():
    print('this is f3')

f3()  #f3 is no longer as its definition.


print('\n')

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print('Elapsed time: {} ms'.format((t2 - t1) * 1000))
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print('Big sum: {}'.format(sum(num_list)))

def main():
    big_sum()

if __name__ == '__main__': main()
