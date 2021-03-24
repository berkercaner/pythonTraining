def main():
    kitten(buffy = 'meow', zilla = 'grr', angel = 'rawr') #it's a dictionary
    x = dict(buffy = 'meow', zilla = 'grr', angel = 'rawr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs): #key word argument
        for k in kwargs:
            print('kitten {} says {}'.format(k,kwargs[k]))
    else:
        print('meow')

if __name__ == '__main__': main()