# passwordGenerator
# this works 8/15/21.

from random import randint
import os

# create characters included in making a password.
letters_str = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
number_str = '0 1 2 3 4 5 6 7 8 9'
symbol_str = '! @ # $ % ^ & * ( ) _ + - .'

# Create character lists to be accessed by indexing.
letters = letters_str.split(' ')
numbers = number_str.split (' ')
symbols = symbol_str.split(' ')

print('Let\'s get some details about the password we\'re creating: ')
letter_count = int(input('How many letters do you want in your password? '))
number_count = int(input('How many numbers to you want in your password? '))
symbol_count = int(input('How many symbols do you want in your password? '))

password = ''

for i in range(0, letter_count): # this might not be pythonic/best practice.
    # adds specified number of random letters to password.
    character = letters[randint(0,25)]
    password = password.__add__(character)

for i in range(0, number_count):
    # appends password with random numbers.
    num = numbers[randint(0, 9)]
    password = password.__add__(num)

for i in range(0, symbol_count):
    # adds random symbols to password.
    symbol = symbols[randint(0, symbol_count)]
    password = password.__add__(symbol)

char_count = letter_count + number_count + symbol_count
password_list = list(password) # Changes password string into a list for indexing characters.

for i in range(0, char_count):
    # Mixes password characters.
    char = password_list.pop(randint(0, char_count-1))
    password_list.insert(randint(0, char_count-1), char)
    print(password_list)

sorted_password = ''
for l in password_list:
    sorted_password = sorted_password.__add__(l)

print(f'\nYour {char_count} character password is: ')
print(sorted_password)