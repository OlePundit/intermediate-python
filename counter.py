#counter
from collections import Counter
#Container that stores the elements as dictionary keys and their counts as disctionary values


a = "aaaaabbbbccc"
my_counter = Counter(a) #output->Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter)


a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter.items())#output->dict_items([('a', 5), ('b', 4), ('c', 3)])


a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter.keys())#output keys

a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter.values())#outputs values


a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter.most_common(1))#outputs most common item

a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter.most_common(2))##outputsthe two most common items

a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter.most_common(1)[0][0])##output->a

a = "aaaaabbbbccc"
my_counter = Counter(a) 
print(my_counter)
print(list(my_counter.elements()))##gives us an iterable






