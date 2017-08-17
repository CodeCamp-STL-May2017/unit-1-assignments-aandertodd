# Add import statement.
from .helpers import alphabet_position, rotate_character

def encrypt(message, key):

    # initialize empty message
    encrypted_message = ''

    # initialize key iterator
    key_iterator = 0
    total_non_alph = 0

    # encrypt letters, let non-alpha characters pass
    for i in range(len(message)):

        if message[i].isalpha():

            # use the non_alph iterator to find the new letter index
            key_letter = key[key_iterator % len(key)]

            key_index = alphabet_position(key_letter)
            encrypted_letter = rotate_character(message[i], key_index)

            encrypted_message += encrypted_letter
            total_non_alph += 1
            key_iterator += 1
        # all non-letters will go here
        else:
            encrypted_message += message[i]


    return encrypted_message

    return encrypted_message
