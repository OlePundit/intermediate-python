"""
Parameters - The variables that are used inside parenthesis while deining a function
Arguments - The values for these parameters


"""


def foo(a,b,c):
    print(a,b,c)

foo(1,2,3) # Positional arguments
foo(a=1,b=2,c=3) #Keyword arguments->order is not iimportant
foo(1,b=2,c=3) #You can use a mix both, but you cannot use a positional argument after a kwarg. But once you do this then they have to be ordered


#default arguments(Must be at the end)
def foo(a,b,c, d=4): 
    print(a,b,c,d)

foo(1,2,3,7)#Output-> 1,2,3,7 i.e you can overite the default



def foo(a,b, *args, **kwargs): #means you can pass any number of postional or keyword arguments
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1,2,3,4,5, six=6, seven=7)


#forced keywords arguments
def foo(a,b, *, c,d): #every parameter after the start must be keyword arguments
    print(a,b,c,d)


foo(1,2,c=3,d=4)


def foo(*args, last): #the first arguments must be positional, and the last must be a kwarg
    for arg in args:
        print(arg)
    print(last)


foo(1,2,3,last=100)


#unpacking a dictionary into a list in our arguments
def foo(a,b,c):
    print(a,b,c)

my_dict={'a':1,'b':2,'c':3}
foo(**my_dict) #if you want to unpack a list then use only on asterisk

#global variables
def foo():
    x = number #if you define a number inside this function its a local variable, the global variable overwrites it
    print('number inside function:', x)

number = 0
foo()


def foo():
    global number
    x = number
    number=3
    print('number inside function:', x)

number = 0
foo()
print(number)


#parameter passing
def foo(x):
    x=5 #Local variable

var=10
foo(var)
print(var)
