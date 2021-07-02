import math

def countTriplets(N, A):
    # Write your code here
    A.insert(0,0)
    cnt=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                x=math.sqrt((A[i]*A[j]*A[k]))
                if isinstance(x,int):
                    cnt=cnt+1
                    print(cnt)
    return cnt   

print(countTriplets(3,[3,6,2]))