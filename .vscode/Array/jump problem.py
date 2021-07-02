def jump(nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True
print(jump([2,3,1,1,4,1,1,2,3,1,2,3]))