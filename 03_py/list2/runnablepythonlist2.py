def big_diff(nums):
    numsmin = nums[0]
    numsmax = nums[0]
    for i in nums:
        if i < numsmin:
            numsmin = i
        if i > numsmax:
            numsmax = i
    return numsmax - numsmin


print(big_diff([10, 3, 5, 6])) 
        
 

  

def centered_average(nums):
    numsmin = nums[0]
    numsmax = nums[0]
    for i in nums:
        if i < numsmin:
            numsmin = i
        if i > numsmax:
            numsmax = i
    count = 0
    for i in nums:
        if i != numsmin and i != numsmax:
            count += i
    return count / len(nums)

print(centered_average([1, 2, 3, 4, 100]))
  
