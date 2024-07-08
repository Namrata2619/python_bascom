# right align triangle:

for x in range(1,6):
    
    # space
    for z in range(x,5):
        print("  ",end="")
    
    # star
    for y in range(1,x+1):
        print("* ",end="")
    
    print()
print()

# Upside down Pyramid
   
#       *********
#        *******
#         *****
#          ***
#           *

for x in range(1,6):
    
    # space
    for z in range(1,x):
        print("  ",end="")
    
    # star
    for y in range(1,12-(2*x)):
        print("* ",end="")
    
    print()
        
    
# pyramid
#               *       1
#              ***      3
#             *****     5
#            *******    7
#           *********   9

for x in range(1,6):
    
    # space
    for z in range(x,5):
        print("  ",end="")
    
    
    #star
    for y in range(1,(2*x)):
        print("* ",end="")
    
    print()

