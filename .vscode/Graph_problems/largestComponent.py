def largestComponentsCount(graph):
    largestcount=0
    visited=set()
    for i in graph:       
        size =helper(graph,i,visited)
        if size>largestcount:
            largestcount=size
    return largestcount

def helper(graph,src,visited):
    if src in visited:
        return 0
    visited.add(src)
    size=1
    for i in graph[src]:
        size=size+helper(graph,i,visited)
    return size
graph={0:[8,1,5],1:[0],2:[3,4],5:[0,8],8:[0,5],3:[2,4],4:[3,2]}
print(largestComponentsCount(graph))    
    