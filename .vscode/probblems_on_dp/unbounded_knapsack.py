def knapsack(w=[1,2,3],p=[2,4,7],m_w=17):
    m=min(w)   
    def helper(w,p,m_w,m):
        max_it=0
        s=0
        if m_w<0:
            return float('-inf')
        for i in range(len(w)):
            s=helper(w,p,m_w-w[i],m)
            if s!=float('-inf'):
                max_it=max(s+p[i],max_it)
        return max_it      
    return helper(w,p,m_w,m)    

print(knapsack())
    
    