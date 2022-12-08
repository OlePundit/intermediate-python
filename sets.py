#sets

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens) #returns all the numbers in both sets

print(u)

i = odds.intersection(primes) #returns only the numbers present in both sets
print(i)

diff = odds.difference(primes) #returns the numbers that are present in one set but not the other
print(diff)


diff = odds.symmetric_difference(primes) #returns the all the numbers that are present in the sets except the ones that are present in both
print(diff)




print(odds.issubset(primes)) #prints false, checks if one set is a subset of the other
print(odds.issuperset(primes)) #prints false, checks if one set is a superset of the other
print(odds.isdisjoint(primes)) #prints false, checks whether there are same elements


odds.update(primes) #Prints all the numbers in both sets without repetition
print(odds)

odds.intersection_update(primes) #updates the odds to print only the numbers found in both. Can perform the same operation for difference, and symmetric_difference
print(odds)

a = frozenset([1,2,3,4]) #immutable