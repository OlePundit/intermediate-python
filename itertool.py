from itertools import product, permutations,combinations, combinations_with_replacement,accumulate,groupby,count,cycle,repeat
import operator
a=[1,2]
b=[3,4]
prod = product(a,b) #output->[(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(prod))


a=[1,2,3]
perm = permutations(a) #all the possible sequences
print(list(perm))

a=[1,2,3]
perm = permutations(a, 2) #specifies the length of the permutations
print(list(perm))

a=[1,2,3,4]
comb = combinations(a,2) #all possibles combinations (difference between a combination and permutation is that in combination the numbers cannot repeat even if they are in a different sequence)
print(list(comb))

a=[1,2,3,4]
comb = combinations(a,2) 
print(list(comb))
comb_wr = combinations_with_replacement(a, 2) #output->[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print(list(comb_wr))

a=[1,2,3,4]
acc = accumulate(a) #cumulative(by default computes the sums)
print(a)
print(list(acc))

a=[1,2,3,4]
acc = accumulate(a, func=operator.mul) #cumulative multiplication
print(a)
print(list(acc))

a=[1,2, 5, 3,4]
acc = accumulate(a, func=max) #output->[1, 2, 5, 5, 5] (returns the max value as it iterates)
print(a)
print(list(acc))

#groupby is an iterator that returns keys and groups form an iterable
def smaller_than_3(x):
    return x<3

a=[1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))



a=[1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3) #short form of the same function above using lamda functions
for key, value in group_obj:
    print(key, list(value))

persons = [{'name':'Tim', 'age': 25}, {'name':'Dan','age':25},
            {'name':'Lisa','age':27}, {'name':'claire','age':28}]

group_obj = groupby(persons, key=lambda x: x['age']) #short form of the same function above using lamda functions
for key, value in group_obj:
    print(key, list(value))

#infinite iterators
for i in count(10): #starts at ten
    print(i)
    if i == 15: #if you dont add a breaking condition it will continue forever
        break

a=[1,2,3]
for i in cycle(a): #loops over the same list infinitely unless there is a break condition
    print(i)

a=[1,2,3]
for i in repeat(1): #repeats only one, could add a second argument to signify how many times you want to repeat for
    print(i)