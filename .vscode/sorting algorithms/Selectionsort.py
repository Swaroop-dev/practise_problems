#swapping at the end instead-selection sort

def selectionsort(arr=[1,4,23,6,-1]):
    n=len(arr)
    for i in range(n):
        mv=i
        for j in range(i+1,n):
            if arr[j]<arr[mv]:
                mv=j
        arr[i],arr[mv]=arr[mv],arr[i]        
    return arr    

print(selectionsort())