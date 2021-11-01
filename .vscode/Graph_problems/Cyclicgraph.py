#converting given input to adjacency list

def adjlist(edges):
    graph={}
    for i in edges:
        a,b=i
        if  graph.get(a) is None:
            graph[a]=[]
        if  graph.get(b) is None:
            graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph


def hasPath(graph,src,dest,visited=None):
    if visited is None:
        visited =set()
    if src in visited:
        return False    
    if src==dest:return True
    visited.add(src)
    for i in graph[src]:
        if hasPath(graph,i,dest,visited):
            return True
    return False    

def findPath(edges,src,dest):
    graph=adjlist(edges)    
    return hasPath(graph,src,dest)
    
edges=[['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]
# print(adjlist(edges))            
print(findPath(edges,'i','l'))