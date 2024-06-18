name = "namratapandya12"
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.casefold())
print(name.center(20,'*'))
print(name.ljust(20,'*'))
print(name.rjust(20,'*'))
print(name.find('a'))
print(name.split(' ')) # split string
print(name.isalnum())
print(name.replace('namrata', 'nandini')) # replace string
print(name.count('a'))
print(name[7:11]) # get substring
print(name.strip()) # remove unnecesaary space
print(name.lstrip()) # remove leading space
print(name.rstrip()) # remove trailing space

a = 'hello'
b = 'student'
c = 45

print(a +' '+b)

# fstring
print(f"{a} {b} {c}")

price = 4500
print('cloth price is'+' '+str(price))

print(f'price of my cloth is {price:.3f}')

m = 12
n = 13
print(f"sum of {m} and {n} is {m+n}")

value = 3400

print('expensive' if value>3200 else'cheap')

print(f'price is very {('expensive') if value>3200 else ('cheap')}')

salary = 120000
print(f'my salary is {salary:,} rs')


