graph={'a':['c','b'],'b':['d'],'c':['e'],'e':['b'],'f':['e'],'d':[]}

def dfs(graph,src,dest):
    s=[src]
    while len(s)>0:
        cur=s.pop()
        if cur==dest:
            print("pasth exist")
            return
        print(cur,"->",end='')
        # print(graph[cur])
        for i in graph[cur]:
            s.append(i)
            
def bfs(graph,src):
    s=[src]
    while len(s)>0:
        cur=s.pop()
        print(cur,"->",end='')
        # print(graph[cur])
        for i in graph[cur]:
            s.insert(0,i)
                
            
dfs(graph,'a','d')      
# bfs(graph,src='a')      

