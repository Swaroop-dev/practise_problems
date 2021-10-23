def loothouse(A=[10,2,12,11,11,13],i=0,memo=None):
    if memo is None: memo =[None]*(len(A))
    if i>len(A)-1:
        return 0
    
    if memo[i]:
        return memo[i]
    s1=s2=0
    # if not taken:
    s1=A[i]+loothouse(A,i+2,memo)
    s2=loothouse(A,i+1,memo)
    
    n=max(s1,s2)
    memo[i]=n
    return n

# print(loothouse())
def optimizedSoln(arr=[10,2,3,11]):
    n=len(arr)
    # dp=[0]*n
    # dp[0]=arr[0]
    prev1=max(arr[0],arr[1])
    prev2=arr[0]
    for i in range(2,n):
        cur=max(arr[i]+prev2,prev1)
        prev2=prev1
        prev1=cur
        
    return cur    
print(optimizedSoln())