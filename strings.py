
my_string = 'Hello World'
print(my_string.startswith('world')) #returns false
print(my_string.endswith('world')) #returns true
print(my_string.find('o')) #returns the first index that it finds with the given letter, returns -1 if doesnt find it
print(my_string.replace('world', 'universe')) #replaces, if it doesnt find, it returns the original string

my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)

my_string = 'how,are,you,doing'
my_list = my_string.split(",") #comma delimited
new_string = ' '.join(my_list) #if you want a space put it in the first argument
print(new_string)


my_list = ['a'] * 6
print(my_list)

my_string = ''
for i in my_list:
    my_string += i  #bad
print(my_string)


my_string = ''.join(my_list)
print(my_string)     #good-> much faster



#%, .format(), f-strings
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)


var = 3
my_string = "the variable is %d" % var #output->the variable is 3
print(my_string)

var = 3.476574
my_string = "the variable is %f" % var #output->the variable is 3.476574(by default it has 6 digits after decimal)
print(my_string)

var = 3.476574
my_string = "the variable is %.2f" % var #output->the variable is 3.476574(specifies decimal places)
print(my_string)

var = 3.476574
my_string = "the variable is {}".format(var) #output->new format of doing it
print(my_string)

var = 3.476574
my_string = "the variable is {:.2f}".format(var) #specifies decimal places
print(my_string)

var = 3.476574
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2) #multiple variables
print(my_string)

var = 3.476574
var2 = 6
my_string = f"the variable is {var} and {var2}" #newest format using f-strings. Python 3.6+
print(my_string)

var = 3.476574
var2 = 6
my_string = f"the variable is {var*2} and {var2}" #You can also mathematical operations
print(my_string)




