# Add import statement.
from .helpers import alphabet_position, rotate_character

def encrypt(message, key):

    encrypted_message = ''

    for i in range(len(message)):

        if message[i].isalpha():

            current_letter = message[i]
            key_letter = key[i % len(key)]
            key_index = alphabet_position(key_letter)
            encrypted_letter = rotate_character(current_letter, key_index)
            
            # add new letter to encrypted_message
            encrypted_message += encrypted_letter

        elif message[i] == ' ' or not message[i].isalpha():
            encrypted_message += ' '


    return encrypted_message
