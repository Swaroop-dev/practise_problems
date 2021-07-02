def maxArea( height):
    h=len(height)
    ouput=-1000000
    for i in range(h):
        for j in range(i+1,h):
            temp=min(height[i],height[j])*(j-i)
            ouput=max(ouput,temp)
    return ouput 
print(maxArea([1,8,6,2,5,4,8,3,7]))
         
    