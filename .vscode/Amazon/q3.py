s="abcdcdddeeeeeiiioou"
result=[]
vowels="aeiou"
for i in vowels:
    if i in s:
        x=s.count(i)
        result.append([i,x])
sortedlist=sorted(result,key=lambda x:x[1],reverse=True) 
return
print (sortedlist)   
# print(s.count('d'))
