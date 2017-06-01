# Add import statement.
from .helpers import alphabet_position, rotate_character

def encrypt(message, key):

    encrypted_message = ''
    total_non_alph = 0
    for i in range(len(message)):

        if message[i].isalpha():
            
            key_letter = key[total_non_alph % len(key)] #this is an equation to find key index
            
            key_index = alphabet_position(key_letter)
            encrypted_letter = rotate_character(message[i], key_index)
            
            encrypted_message += encrypted_letter
            total_non_alph += 1
        else:
            encrypted_message += message[i]


    return encrypted_message
