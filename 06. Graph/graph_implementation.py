


graph=dict()
vertices=set()


def add_edge(u,v):

    if u in graph:
        graph[u].append(v)
    else:
        graph[u]=[v]

    vertices.add(u)
    vertices.add(v)


def DFS(node,visited=set()):

    if node in visited:
        return

    visited.add(node)
    print(node,end="  ")

    if node not in graph:
        return

    for adj in graph[node]:

        DFS(adj,visited)


    
def BFS(node):

    queue=[node]

    visited=set()

    print()

    while queue:

        a=queue.pop(0)

        if a in visited:
            continue

        print(a,end="  ")
        visited.add(a)

        if a not in graph:
            continue

        for adj in graph[a]:
            queue.append(adj)

    print()

        


def main():

    add_edge(1,2)
    add_edge(1,3)
    add_edge(1,4)
    add_edge(2,5)
    add_edge(2,6)
    add_edge(3,6)
    add_edge(3,7)
    add_edge(4,7)


    BFS(1)

    DFS(1)


# main()