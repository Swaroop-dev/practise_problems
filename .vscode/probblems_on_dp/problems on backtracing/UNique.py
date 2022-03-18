class Solution:
    def uniquePathsIII(self, grid) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return self.helper(grid,i,j,m,n,visited)
                
                
    def helper(self,grid,src,des,m,n,visited):
        if not  (0<=src<m and 0<=des<n and ((src,des) in visited)):
            return 0
        if grid[src][des]==2 and (len(visited)==0):
            return 1
        if grid[src][des]==-1:
            return 0
                
        visited.append((src,des))
        s1=s2=s3=s4=0
        
        #up
        if 0<=src-1<m and 0<=des<n and ((src-1,des) in visited):
            s1=self.helper(grid,src-1,des,m,n,visited)
        #down    
        if 0<=src+1<m and 0<=des<n and ((src+1,des) in visited):
            s2=self.helper(grid,src+1,des,m,n,visited)
        #left    
        if 0<=src<m and 0<=des-1<n and ((src,des-1) in visited):
            s3=self.helper(grid,src,des-1,m,n,visited)
        #right    
        if 0<=src<m and 0<=des+1<n and ((src,des+1) in visited):
            s4=self.helper(grid,src,des+1,m,n,visited)  
            
        visited.pop((src,des))   
        
        return s1+s2+s3+s4
    
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]    
s1=Solution()
print(s1.uniquePathsIII(grid))    