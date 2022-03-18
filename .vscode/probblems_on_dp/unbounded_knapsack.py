#unbounded knapsack problem

def knapsack(w=[1,2,3],p=[2,4,7],m_w=17):
    # m=min(w)   
    def helper(w,p,m_w):
        max_it=0
        s=0
        if m_w<0:
            return float('-inf')
        for i in range(len(w)):
            s=helper(w,p,m_w-w[i])
            if s!=float('-inf'):
                max_it=max(s+p[i],max_it)
        return max_it      
    return helper(w,p,m_w)    

print(knapsack())
    
def optimised(w,p,n):
    
    dp=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(len(w)):
            if w[j]<=i:
                dp[i]=max(dp[i],dp[i-w[j]]+p[j])
    return dp[-1]        
            
print(optimised(w=[1,2,3],p=[2,4,7],n=17))        