#longest common palindrome
#rodcutting problem
#longest common sequence and subsequence
#longest common increasing sequence
#deletions required to convert string into palindrom


def longest_common_sequence(X,Y):
    if X is None or Y is None:
        return None
    m=len(X)
    n=len(Y)
    t=[[0 for i in range(n+1)] for j in range(m+1)]
    for i  in range(1,m+1):
        for j in range(1,n+1):
            if  X[i-1]== Y[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])    
    return t[m][n]            

# print(longest_common_sequence(X="XMJYAUZ",
#     Y = "MZJAWXU"))

def rod_cutting_problem(p,n):
    t=[0 for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,i+1):
            t[i]=max(t[i],p[j-1]+t[i-j])
    return t[-1]      

def longest_increasing_subsequence(S):
    output=[0 for i in range(n)]
    output[0]=1
    for i in range(1,n):
        for j in range(0,i):
            if S[j]<S[i] and output[i]<output[j]:
                output[i]=output[j]
        output[i]=output[i]+1
    print(max(output))            
                
# longest_increasing_subsequence(S=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])   


def deletions_required(S):
    n=len(S)
    if n==0:
        return 0
    S1=S[::-1]
    o1=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if S[i-1]==S1[j-1]:
                o1[i][j]=o1[i-1][j-1]+1
                
            else:
                o1[i][j]=max(o1[i-1][j],o1[i][j-1])
    return  n-o1[-1][-1]           
# print(deletions_required(S="ACBCDBAA"))    

def shortest_path():
   cost = [
        [0, 25, 20, 10, 105],
        [20, 0, 15, 80, 80],
        [30, 15, 0, 70, 90],
        [10, 10, 50, 0, 100],
        [40, 50, 5, 10, 0]
    ] 
   for i in range(len(cost)):
       return min()