def shortestPath(graph,src):
    q=[src]
    visited=set()
    while len(q)>0:
        cur=q.pop()

        if not (cur in visited):
            visited.add(cur)
            for i  in graph[cur]:
                q.insert(0,i)
        