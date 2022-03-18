#printing subests of an array
#printing paths from an matrix

def subset_prob(arr,i,n,osf):
    if i==n:
        v="["+ osf +"]"
        print(v)
        return
    subset_prob(arr,i+1,n,osf+" "+str(arr[i]))
    subset_prob(arr,i+1,n,osf)
    
# subset_prob([0,1,2],0,3,"")    
    
    
total=0    
def path_matrix(i,j,n,m,ospf):
    global total
    if i==n-1 and j==m-1:
        print(ospf)
        total=total+1
        return
    if i>n-1 or j>m-1:
        return
    path_matrix(i+1,j,n,m,ospf+"D")
    path_matrix(i,j+1,n,m,ospf+"R")
        
        
# path_matrix(0,0,3,3,"")     
# print(total)   

def printing_permutation(pref,rem):
    if len(rem)==0:
        print(pref)
        return
    for i in range(0,len(rem)): 
        v=rem[i]
        ros=rem[:i]+rem[i+1:]
        printing_permutation(pref+v,ros)
        
printing_permutation("", "ABC")   