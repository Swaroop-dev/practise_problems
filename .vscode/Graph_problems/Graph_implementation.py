# implementing directed Unweighted graph
#implementing directed weighted graph

class Edge:
    def __init__(self,src,dest,dir=True):
        self.src=src
        self.dest=dest
        self.dir=dir
        
class unweighted_graph:
    def __init__(self,edges,N):
        self.adj=[[]for i in range(N)]
        
        for j in edges:
            self.adj[j.src].append(j.dest)
            if j.dir:
                self.adj[j.dest].append(j.src)
            
    def printing_from_inside(self):
        for i in range(len(self.adj)):
            for j in self.adj[i]:
                print(f'({i}->{j})',end=" ")
            print()    
            
                    
            
def printing_graph(graph):
    for src in range(len(graph.adj)):
        for dest in graph.adj[src]:
               print(f'({src}->{dest})',end=" ")
        print()
           
edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0,False),
             Edge(3, 2), Edge(4, 5)]
ug1= unweighted_graph(edges,N=6)
# printing_graph(ug1)        
ug1.printing_from_inside() 


#weighed graph impelmentation

class WeightedEdge:
    def __init__(self,src,dest,weight):
        self.src= src
        self.dest= dest
        self.weight= weight
        
# class weighted_graph: 
#     def __init__(self,edges,N):
        
        
                     
                        
