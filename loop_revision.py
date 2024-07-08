# i = 1
# while i<=10:
#     print(i)
#     i+=1

# for i in range(1,11):
#     print(i)

list = [12,34,567,'bascom', 'vastrapur']

# for i in list:
#     print(i)
# for i in 'bascom':
#     print(i)

# for i in range(len(list)):  # to find out list length
#     print(i)

# check whether the num is prime or not
# num = int(input("Enter a number: "))

# if num<2:
#     print('not prime')
# else:
    
#     flag = 0
    
#     for x in range(2,num): # 2.....num
#         if(num%x==0):
#             flag = 1
#             break
#     if(flag==0):
#         print('prime')
#     else:
#         print('not prime')

# find number of vowel, consonant or symbol or number inside a string

str = input("Enter string:")

v = 0
c = 0
d = 0
s = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']

for i in str:
    if(i.isalpha()):
        if(i in vowels):
            v = v+1
        else:
            c = c+1
        
    elif(i.isdigit()):
        d = d+1
    else:
        s = s+1
print(f"vowels are:{v}\nconsonents are:{c}\ndigits are:{d}\nsymbols are:{s}")



