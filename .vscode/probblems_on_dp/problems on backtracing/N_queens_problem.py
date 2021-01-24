# Nqueens problem- no of ways placing N queens such that no queens attack each other
#optimised using bitset

n=4
X=[[False]*n for _ in range(n)]
totalWays=0

def isSafe(row,col):
    #column check
    for i in range(row-1,-1,-1):
        if X[i][col]==True:
            return False
    
    #right diagnol check
    i=row
    j=col
    while(i>=0 and j<n):
        if X[i][j]==True:
            return False   
        i=i-1
        j=j+1 
        
    #left diagnol check
    i=row
    j=col
    while(i>=0 and j>=0):
        if X[i][j]==True:
            return False   
        i=i-1
        j=j-1
    return True    
            
def countQueens(curr_row):
    global totalWays
    if curr_row==n:
        totalWays=totalWays+1
        return
    for i in range(n):
        if(isSafe(curr_row,i)):
            X[curr_row][i]=True
            countQueens(curr_row+1)
            X[curr_row][i]=False
    return totalWays

print(countQueens(0))
