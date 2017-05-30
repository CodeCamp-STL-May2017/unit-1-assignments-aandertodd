alph = 'abcdefghijklmnopqrstuvwxyz'
alph2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    

def alphabet_position(letter):

     
    
    if letter < 'a':
        return alph2.find(letter)
    else:
        return alph.find(letter)

def rotate_character(char, rot):
    
    newletter = (alphabet_position(char) + rot) % 26
    newposition = alph[newletter] or alph2[newletter]

    if char in alph2:
        return newposition.upper()
    if char in alph:
        return newposition.lower()
    else:
        return char
