def get_initials(fullname):
    #get first init
    first_init = fullname[0]
    #find ' '
    for char in range(len(fullname)):
        if fullname[char] == ' ':
#for every instance of ' ', return the character to the right as an upper().
            next_init = fullname[char + 1]
            first_init += next_init
            # while char == next_init:
    return first_init.upper()