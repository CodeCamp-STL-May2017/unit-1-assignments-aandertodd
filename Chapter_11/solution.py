def get_country_codes(nums):

    
    codes = nums.replace('$','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    return_code = ''.join([code for code in codes if not codes.isdigit()])
    
    
        
        
            
    
    
 
    
    
    return return_code