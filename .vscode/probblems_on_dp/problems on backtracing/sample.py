#backtracking
#permmutation of a string using backtracking
    

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