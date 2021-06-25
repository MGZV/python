import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

length = int(input('Enter number of characters: '))
password = ''
for i in range(length):
    password += random.choice(chars)
print(password)