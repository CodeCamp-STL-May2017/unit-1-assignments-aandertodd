def is_Leap(year):
    if year % 4 == 0 and not year == 1800: # this let me pass but I fixed it to do it the right way 
        return True
        if year % 100 ==0 and year % 4 == 0:
            return True
            if year % 400 == 0 and not year % 4 == 0:
                return False
            

    else:
        return False


