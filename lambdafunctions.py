# lambda function

# in regular function:

# def function_name(arguments/parameter):
#            function body

# lambda arguments/parameter : body
# function without anyname

x = lambda a : print(a)    # one liner function

x(12)   # calling of lambda function

sum = lambda a,b : a+b

print(sum(12,13))    # lambda function with two parameter

# function inside a function

def takeNumber(num):
    print(num/10)

takeNumber(sum(10,20))