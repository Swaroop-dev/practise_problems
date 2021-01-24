# knights tour problem

n = 5
visited = [[False]*n for _ in range(n)]
grid = [[-1]*n for _ in range(n)]


def isSafe(i, j):
    return i >= 0 and j >= 0 and i<n and j<n and visited[i][j] == False


def KnighsTour(i, j, cnt):
    if cnt == n*n-1:
        grid[i][j]=cnt
        print(grid)
        return
    
    if cnt>=n*n:
        return
    
    xdir = [-2, -2, -1, -1, 2, 2, 1, 1]
    ydir = [1, -1, 2, -2, 1, -1, 2, -2]
    visited[i][j] = True
    grid[i][j] = cnt
    for k in range(8):
        if(isSafe(i+xdir[k], j+ydir[k])):
            KnighsTour(i+xdir[k], j+ydir[k], cnt+1)
    grid[i][j] = None
    visited[i][j] = False


KnighsTour(0, 0, 0)
