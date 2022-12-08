# small anonymous function defined without a name
from functools import reduce

add10 = lambda x: x+10 #(function with one argument and then it adds 10 to the argument and returns the result)
print(add10(5))

mult = lambda x,y: x*y
print(mult(2,7))

#sorted
points2D = [(1,2),(15,1),(5,1),(10,4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

points2D = [(1,2),(15,1),(5,1),(10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1]) #Gets sorted according to y index
print(points2D)
print(points2D_sorted)

points2D = [(1,2),(15,1),(5,1),(10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) #Gets sorted according to sums
print(points2D)
print(points2D_sorted)


#map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x:x*2, a) #each element get multiplied by 2
print(list(b))


#filter(func, seq)#returns all functions for which the element evaluates to true
a = [1,2,3,4,5,6]
b = filter(lambda x:x%2==0, a) 
print(list(b))


#reduce(func, seq)#repeatedly applies the function to the element and returns a single value
a = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)






