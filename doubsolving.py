# print first digit and last digit of any number:

num = int(input("Enter any Number: "))

last_digit = num%10
new_last_digit = 0

while num!=0:
    new_last_digit = num%10
    num = num//10

print(f"Last digit: {last_digit}")
print(f"First digit = {new_last_digit}")