def nextgreatest(nums):
    
        
    for i in range(len(nums)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                return nums
    return sorted(nums)

print(nextgreatest(nums=[2,2,3]))