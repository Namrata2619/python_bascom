# operators
# symbols
# < > <= >= != == ( ==, eqaulity operator)
# = assignment operator

#  a = b
a = 15 
b = 13

# if
if a < b: # returns boolean value (whether is is true or false)
    print("a is less than b")
else:
    print("a is greater than b")
    
    

a = 12
b = 99
c = 100
# find max from 3 numbers using if elif else 

if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
else: # a<b
    if b<c:
        print("c is max")
    else:
        print("b is max")
        
# find min from 3 numbers using if elif else

a = 4
b = 2
c = 9

if b<a:
    if b<c:
        print("b is min")
    else:
        print("c is min")
else: # b>a
    if a<c:
        print("a is min")
    else:
        print("c is min")

# take input from user

#a = int(input("enter one number =>"))
#print(a)
#print(type(a))

b = 18
c = 2

a = b%c  # modulo % gives the remainder
print(a)

# take year from user and check if the years is leap or not

year = int(input("enter a year =>"))

if year%4==0:
    print("years is leap")
else:
    print("year is not leap")


# take one number from user and check whether it is odd oor even

number = int(input("enter one number"))

if number%2==0:
    print("number is even")
else:
    print("number is odd")
    
# take celcius from user and convert it into ferenheit

#celcius = float(input("enter temperature =>"))

#g = (9/5)*celcius + 32

#print(g)

#ferenheit = (9/5)*celcius + 32
print("ferenheit is:" + str((9/5)*(float(input("enter temperature =>"))) + 32))











    
    
    
    

    
