# script to do a ceaser cipher.


letters = 'abcdefghijklmnopqrstuvwxyz'

directions = input("Type [e]encode to encrypt or [d]decode to decrypt: ")
plain_text = input("Enter you message to encrpyt: \n")
shift = int(input("Type the shift number: \n"))

def encrypt(text, shift):
    encoded_text = ''
    for letter in text:
        letter_position = letters.index(letter)
        new_position = letter_position + shift
        if new_position > 25:
            new_position = new_position - 25
        new_letter = letters[new_position]
        encoded_text += new_letter
    print(encoded_text)

encrypt(plain_text, shift)

