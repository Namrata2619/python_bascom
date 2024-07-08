# symbols

# arithmatic operators

# + - / * ** % // (// is floor division)

a = 12
b = 7

print(a**b)
print(a//b)

# assignment operator
# = += -= /= %= //= **=
a = 10
a += 5
print(a)

a = 12
a %= 10 # 12%10 remainder 2. and that new value assigned to a

print(a)

# membership operator
# in, not in
list1 = [1,2,3,4,5]
print(5 in list1)
print(6 not in list1)
print(12 in range(0,20))

# logical operator
# and, or, not
a = 10
b = 20
print(a > 5 and b > 10)
print(a > 5 or b > 10)
print(not a > 5)

# identity operator
# is, is not
a = 10
b = 10
print(a is b)
print(a is not b)
print(type(a) is int)

# what else can i do in is operator
# is operator checks if both variables are pointing to same object in memory
a = [1,2,3]
b = [1,2,3]
print(a is b) # false because they are two different objects in memory
print(a == b) # true because they have same value
# but if we do
a = b
print(a is b) # true because they are pointing to same object in memory




