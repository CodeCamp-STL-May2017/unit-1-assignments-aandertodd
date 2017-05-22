def mirror(text):
    rev = reverse(text)
    mir = text + rev
    for i in text:
        if i == 'a':
            mir = mir.upper()
    return mir


def reverse(text):
    
    r = ''
    for i in text:
        r = i + r 
    
    return r