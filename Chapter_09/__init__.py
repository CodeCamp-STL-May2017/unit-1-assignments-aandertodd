def get_initials(fullname):
    #get first init
    first_init = fullname[0]
    #find ' '
    for char in range(len(fullname)):
        if fullname[char] == ' ':
#for every instance of ' ', return the character to the right as an upper().
            next_init = char + 1

            # while char == next_init:
            return fullname.upper()[0] + fullname.upper()[next_init] 


