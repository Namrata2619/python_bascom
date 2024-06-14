# str  - string data type
a = "bascom"
print(type(a))

a = 12

print(type(a))

a = 12.34
print(type(a))

a = 2 + 2j

print(type(a))



list = [] # list is a datatype we can store multiple values inside it. mutable datatype
values = [12, "hello", 12.34 ]

print(type(values))

# in list range starts with 0 ondex and so on
print(values[2])
values [2] = 99.99
print(values)

# if you want to add values to your range, use append function
values.append("namrata")
print(values)

# if you want to store values at particular index we use insert funtion
values.insert(2,4.4)
print(values)

# if you want to remove some value
values.remove('namrata')
print(values)

values.remove(values[3])
print(values)
del values[2]
print(values)

# if you want to print range
print(values[0:2])

data = [12,14,"hello",'a',45.45]

new_data = data[1:3] # reassign part Range
print(new_data)
print(type(new_data))
f = data[4]
print(type(f))

list1 = [1,2,3,4,5]
list2 = [9,8,7,6]
list3 = list1+list2
print(list3)

# tuple = can't be reassigned values and length can't be changed
fruits = (12, 'hello', 23.45)
print(fruits)
print(type(fruits))
print(fruits[0])

# range
x = range(6) # used in loops
print(x)

# dictionary (used to fetch data from any servers or websites )
# stores multiple values like list but stores as key : VALUE

employee = {"name" : "namrata", "email" : "123@gmail.com", "address" : "sarkhej"}
print(employee)
print(type(employee))

name = [] # empty list // then append  // insert
addresses = {} # empty dictionary
print(employee["address"])
employee[3] = "Hi" #directory value reassign
print(employee[3]) 
# to add  values into empty dictonary

addresses.update({"first name": "krishna", "last name": "pandya"})

print(addresses)

addresses.update({"age":"45"}) # to add values we use update funtion

print(addresses)

# to remove values in dictionary data type
addresses.pop("age")
print(addresses)

addresses.popitem()
print(addresses)

addresses.clear() # claer funtion clear the data inside variable
print(addresses)

# del (to delete variable)

del addresses

## set Data type

voo = {'hello',23,45.4,'h'}
#it is unordered data type
print(voo)
# we can not cahnge data but can be added or removed

voo.add("coco")
print(voo)

voo.remove(45.4)
print(voo)

# we can not add same item

voo.add(23)
print(voo)

voo.remove(23)
print(voo)

print(len(voo)) # find the length

##frozenset = function

my_list = [1,2,3,"hello"]
my_new_list = frozenset(my_list)

print(my_new_list)
print(type(my_new_list))
# frozenset function freeze the datadtype and it doesn't allow crut operation

##boolean data type
islogin = 0
print(bool(islogin))
my_expression = 12>13
print(my_expression)

## none datatype
x = None
print(x)
print(type(x))

# datatype completed









