# passwordGenerator
# this works 8/15/21.

from random import randint
import random
import os

# create characters included in making a password.
letters_str = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
letters_str += letters_str.upper()
number_str = '0 1 2 3 4 5 6 7 8 9'
symbol_str = '! @ # $ ^ * _ + - .'

# Create character lists to be accessed by indexing.
letters = letters_str.split(' ')
numbers = number_str.split (' ')
symbols = symbol_str.split(' ')

print()
print('_' * 60)
print('Let\'s get some details about the password we\'re creating: ')
letter_count = int(input('How many letters do you want in your password? '))
number_count = int(input('How many numbers to you want in your password? '))
symbol_count = int(input('How many symbols do you want in your password? '))

password = ''

for i in range(0, letter_count): 
    # here is an alternative compared to the next two for loops.
    password += random.choice(letters)

for i in range(0, number_count): # this might not be pythonic/best practice.
    # appends password with random numbers.
    num = numbers[randint(0, 9)]
    password = password.__add__(num)

for i in range(0, symbol_count):
    # adds random symbols to password.
    symbol = symbols[randint(0, symbol_count)]
    password = password.__add__(symbol)

# Change password string into a list so it can be indexed.
password_list = list(password)

char_count = letter_count + number_count + symbol_count

for i in range(0, char_count):
    # Mix password characters.
    char = password_list.pop(randint(0, char_count-1))
    password_list.insert(randint(0, char_count-1), char)

# Convert list back to a password string.
mixed_password = ''
for i in password_list:
    mixed_password += i

print(f'\nYour {char_count} character password is: ')
print(mixed_password)