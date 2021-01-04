
'''

        0--->1--->2
        |    |  
        |    |
        |    
        3--->4--->5

    Start with 1
        1. We will mark this as visited
        2. We call recursion on the next to that if it is not visited.
'''

def depthFirstSearch(graph,vertices,current,visited,result):

    result.append(current)
    visited[current] = True
    for i in graph[current]:
        if visited[i] == False:
            depthFirstSearch(graph,vertices,i,visited,result)
    

vertices = 4
edges = 3
graph = {i : [] for i in range(0,vertices)}
for i in range(0,edges):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
visited = [False for i in range(0,vertices)]
result = []
depthFirstSearch(graph,5,0,visited,result)
print(result)