def analyze_text(text):

    
    letter_counter = 0
    e_counter = 0

    
    for char in text:

        
        if char.isalpha():
            letter_counter = letter_counter + 1
            if char == 'e' or char == 'E':
                e_counter = e_counter + 1
    
    percentage = (e_counter / letter_counter * 100)

    answer = answer = "The text contains " + str(letter_counter) +" alphabetic characters, of which " + str(e_counter)+" ("+str(percentage) +"%) are 'e'."
    return answer

