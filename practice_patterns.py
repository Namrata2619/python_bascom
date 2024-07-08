# *
# **
# ***
# ****
# *****

for x in range(1,6):
    for y in range(1,x+1):
        print("*",end="")
    print()
print()
    
#       *
#      **
#     ***
#    ****
#   *****   

for x in range(1,6):
    
    #space
    for z in range(x,5): # (1 5) (2 5) (3 5) (4,5) (5,5)
        print(" ",end="")
    #star
    for y in range(1,x+1):
        print("*",end="")
    print()
print()

# Upside down Pyramid
   
# *********
#  *******
#   *****
#    ***
#     *

for x in range(1,6):
    
    # space
    for z in range(1,x): # (1,0) (2,1) (3,2) (2,3) (1,4)
        print("  ",end="")
        
    # star
    for y in range(1,12-(2*x)): # (1,9) (2,7) (3,5) (4,3) (5,1)     
        print("* ",end="")
    print()

for x in range(1,6):
    
    # space
    for z in range(x,5): # (1,5) (2,4)....
        print("  ",end="")
        
    # star
    for y in range(1,(2*x)): # 
        print("* ",end="")
    print()
print()


# 1. Rectangle and Square Pattern

# *****
# *****
# *****
# *****
# *****

y = 0

for x in range(1,6):
    
    for y in range(1,6):
        print("*",end="") # 
    print()
print()
    
# 2. Hollow Square Pattern

# *****
# *   *
# *   *
# *   *
# *****

for x in range(1,6):
    
    for y in range(1,6):
        if (x==1 or x==5 or y==1 or y==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    print()
    
# 3.Hollow Square Pattern with Diagonal
# *****
# ** **
# * * *
# ** **
# *****

for x in range(1,6):
    
    for y in range(1,6):
        if (x==1 or x==5 or y==1 or y==5 or x==y or x+y==6):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    print()
    
# 4. Rhombus Pattern

#      *****
#     *****
#    *****
#   *****
#  *****

for x in range(1,6):
    
    #space
    for z in range(x,6):
        print(" ",end="")
    
    #star
    for y in range(1,6):
        print("*",end="")
    print()
print()

# 5.Hollow Rhombus Pattern
#      *****
#     *   *
#    *   *
#   *   *
#  *****

for x in range(1,6):
    
    #space
    for z in range(x,6):
        print(" ",end="")
    
    #star
    for y in range(1,6):
        if(x==1 or x==5 or y==1 or y==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    

