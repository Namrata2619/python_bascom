# heart pattern

print()

for x in range (3,6):
    
    # space
    for z in range (x,5):
        print(" ",end="")
    
    # star
    for  y in range(1,(2*x)):
        print("*",end="")
    
     # space
    for a in range (1,(11-(2*x))):
        print(" ",end="")
    
    # star
    for  b in range(1,(2*x)):
        print("*",end="")     
 
    print()

# lower part

for x in range (1,11):
    
    #space
    for z in range(1,x+1):
        print(" ",end="")
    #star
    for y in range(1,(19-(2*x))):
        print("*",end="")
    print()