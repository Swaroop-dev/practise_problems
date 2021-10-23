def path(arr,n,m,i,j,visited=None):
    def isSafe(arr,n,m,i,j,visited):
        if i>=0 and j>=0 and i<n and j<m and visited[i][j]==False:
            if arr[i][j]==1 or arr[i][j]==9:
                return True
        return False
       
    
    if visited is None:
        visited=[ [False]*(m+1) for _ in range(n)]
        
    
    
    if not isSafe(arr,n,m,i,j,visited):
        return 100000
    if arr[i][j]==9:
        return 0
    visited[i][j] = True
    ## right

    x=1+min(path(arr,n,m,i,j+1,visited),path(arr, n, m, i+1, j, visited),path(arr, n, m, i,j-1,visited) )
         
    
    
    return x   
          
print(path([[1,0,0],[1,0,0],[1,9,1]],3, 3, 0, 0 ) )         