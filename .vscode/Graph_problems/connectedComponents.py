def connectedComponentsCount(graph):
    count=0
    visited=set()
    for i in graph:       
        if helper(graph,i,visited):
            count=count+1
    return count
def helper(graph,src,visited):
   
    if src in visited:
        return False
    visited.add(src)
    for i in graph[src]:
        helper(graph,i,visited)        
    return True    

graph={0:[8,1,5],1:[0],2:[3,4],5:[0,8],8:[0,5],3:[2,4],4:[3,2]}
print(connectedComponentsCount(graph))