# for x in range(1,6):   # outer loop gives no. of rows and # inner loop gives no. of columns
#     for y in range(1,5):
#         print(x,end="")
#     print()
    
# for x in range(1,6):   # outer loop gives no. of rows and # inner loop gives no. of columns
#     for y in range(1,5):
#         print("* ",end="")
#     print()
    
# # 2-D loop gives us matrix
# for x in range(0,6):
#     for y in range(0,6):
#         print(f"{x}{y}",end=" ")
#     print()
# print()

# # for printing diagonal pattern:
# for x in range(1,6):
#     for y in range(1,x+1):
#         print("* ",end="")
#     print()
# print()

# # Hollow Square Pattern:
# for x in range(1,6):
#     for y in range(1,6):
#         if(x==1 or x==5 or y==1 or y==5):
#             print("*  ",end="")
#         else:
#             print("   ",end="")
#     print()
# print()

for x in range(1,6):
    for y in range(1,6):
        if (x==y or x+y==6):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
print()

for x in range(1,6):
    
    for z in range(x,5):
        print("  ",end="")
    
    for y in range(1,x+1):
        print("* ",end="")

    print()
print()

for x in range(1,6):#1 2 3 4 5
    
    for z in range(x,6): # for x=1 => 12345 # x=2 => 2345 and so on..... 
        print("* ",end="")
    print()
    
for x in range(1,6):
    
    for z in range(1,x):
        print("  ",end="")
        
    for y in range(x,6):
        print("* ",end="")
    print()