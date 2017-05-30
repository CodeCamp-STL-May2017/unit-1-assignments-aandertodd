# Add import statement.
from .helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    newstr = ''
    for char in text:
        
        newstr += rotate_character(char, rot)
    return newstr