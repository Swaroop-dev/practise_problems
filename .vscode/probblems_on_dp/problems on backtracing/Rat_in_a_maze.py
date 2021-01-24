#backtracking
#permmutation of a string using backtracking
#rat in a maze problem
    

def permutation_using_backtracking(s,j):
    if len(s)-1==j:
        print(s)
        return
    for i in range(j,len(s)):
        x=s[i]
        y=s[j]
        if i<j:
            s=s[:i]+y+s[i+1:j]+x+s[j+1:]
        elif i==j:
            s=s     
        else:
            s=s[:j]+x+s[j+1:i]+y+s[i+1:]
                
        permutation_using_backtracking(s,j+1)
        
        x=s[i]
        y=s[j]
        if i<j:
            s=s[:i]+y+s[i+1:j]+x+s[j+1:]
        elif i==j:
            s=s         
        else:
            s[:j]+x+s[j+1:i]+y+s[i+1:]
        
# permutation_using_backtracking('ABCD',0)        



#rat in the maze problem
total_paths=0
x=[[0,0,1,0,0,1,0],[1,0,1,1,0,0,0],[0,0,0,0,1,0,1],[1,0,1,0,0,0,0],[1,0,1,1,0,1,0],[1,0,0,0,0,1,0],[1,1,1,1,0,0,0]]

n=len(x[0])
m=len(x)


visited=[[False]*n for _ in range(m)]


def isSafe(i,j):
    return i>=0 and j>=0 and i<m and j<n and visited[i][j]==False

def helper(i,j):
    global total_paths
    if i==m-1 and j==n-1:
        total_paths=total_paths+1
        return
    if (not isSafe(i,j)):
        return
    visited[i][j]=True
    #down
    if i+1<m and  x[i+1][j]==0:
        helper(i+1,j)
    #up
    if i-1>=0 and   x[i-1][j]==0:
        helper(i-1,j)
    #right
    if j+1<n and  x[i][j+1]==0:
        helper(i,j+1)
    #left 
    if j-1>=0 and x[i][j-1]==0:
        helper(i,j-1)  
        
    visited[i][j]=False
    return
    
def rat_in_a_maze():
    helper(0, 0)
    return total_paths

print(rat_in_a_maze())

   