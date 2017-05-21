def is_prime(num):

    if num % 2 == 0 and not num ==2:
        return False
        if num % 3 == 0:
            return False
            if num % 4 == 0:
                return False
                if num % 5 == 0:
                    return False
                    
    elif num <= 1:
        return False                
   
    else:
        return True
    



