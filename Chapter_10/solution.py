def find_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))
    
    average = []
    for num in nums:
        sum = 0
        for total in nums:
            sum += total
            avg = sum/len(nums)
        average.append(avg)
         
        
    return avg
         