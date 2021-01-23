#solving subset using backtracking

def subset_using_backtracking(arr,i,n,v):
    if i==n:
        print(v)
        return
    v.append(arr[i])
    subset_using_backtracking(arr,i+1,n,v)
    v.pop()
    subset_using_backtracking(arr,i+1,n,v)
    
    
subset_using_backtracking([1,2,3],0,3,[])    