## wiggle sort problem 

def wigglesort(arr):
    for i in range(len(arr)-1):
        if i%2==0:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]        
    return arr

print(wigglesort([3,5,2,1,6,4]))