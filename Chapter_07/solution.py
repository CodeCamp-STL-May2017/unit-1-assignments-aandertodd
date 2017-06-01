def is_prime(num):
# TODO implement function
    if num < 2 or num % 2 == 0 and not num == 2:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
        
    return True   
   
        
    



