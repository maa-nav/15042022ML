## Generators

##def hell(x):
##    for i in range(x):
##        yield i**2

#### Prime Generator ####

##def prime_gen(lmt):
##    a = 2
##    while a<lmt:
##        for i in range(2,a):
##            if not a%i :break
##            #else :break
##        else : yield(a)
##        a+=1

###### Fibonacci Series #####

##def fib(lmt):
##    old = 0
##    new = 1
##    while old<lmt:
##        temp = old +new
##        new = old
##        yield old
##        old = temp


######### Decorators ##########

def decorate_it(func):
    def wrapper(*x):
        'this is wrapper func'
        print('This should happen before the func')
        print(func(*x))
        print('part of code that should happen after the func call')
    return wrapper


@decorate_it         #hello = decorate_it(hello)
def hello(*y):
    ' this is hello func'
    return sum(y)


    



















         
    

        
