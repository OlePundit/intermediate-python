def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()


#value = next(g)
#print(value)

#value = next(g)
#print(value)

print(sum(g))

print(sorted(g))


def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)


value = next(cd)
print(value)

print(next(cd))

#IMPORTANCE OF GENERATORS


#Its more efficient to do this
def first_generator(n):   
    num=0
    while num < n:
        yield num
        num += 1


print(list(first_generator(10)))

#than this
def first_generator(n):   
    nums = []
    num=0
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(first_generator(10))


def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b

fib = fibonacci(30)
for i in fib:
    print(i)


#SHORTHAND

mygenerator=(i for i in range(10) if i % 2 ==0)#More efficient
for i in mygenerator:
    print(i)

mylist=[i for i in range(10) if i % 2 ==0]
print(mylist)



