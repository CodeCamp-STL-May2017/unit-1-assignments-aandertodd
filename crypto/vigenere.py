

alph = 'abcdefghijklmnopqrstuvwxyz'
alph2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def alphabet_position(letter):

    if letter < 'a':
        return alph2.find(letter)
    else:
        return alph.find(letter)



def rotate_character(char, rot):
    
    
    newletter_index = (alphabet_position(char) + rot) % 26

    if char in alph2:
        return alph2[newletter_index]
    if char in alph:
        return alph[newletter_index]
    else:
        return char

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




def main():
    user_input = input('Type message: ')
    user_encrypt = input('Encryption Key: ')

    
    print(encrypt(user_input, user_encrypt))

if __name__ == "__main__":
    main()