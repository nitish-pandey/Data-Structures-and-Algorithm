from graph_implementation import simple_graph,directed_graph

# Problem Statement 1: Check for cycle in Undirected graph

# Approach: DFS


def dfs1(g:simple_graph,visited:dict,u,par):


    visited[u]=True

    for v in g.get_neighbour(u):

        if visited[v]==False:
            if dfs1(g,visited,v,u):
                return True

        elif v!=par:
            return True

    return False


def isCyclic_Undirected(g:simple_graph) -> bool:

    visited={}

    for i in g.vertices:
        visited[i]=False

    for u in g.vertices:

        if visited[u]==False:
            if dfs1(g,visited,u,-1):
                return True


    return False





# <--End of Implementation-->


# Problem Statement 1: Check for cycle in Directed graph

# Approach: DFS

def dfs2(g:directed_graph,visited:dict(),v) -> bool:

    if visited[v]==1:
        return True

    if visited[v]==2:
        return False

    visited[v]=1

    for u in g.get_neighbour(v):

        if dfs2(g,visited,u):
            return True

    visited[v]=2

    return False


def isCyclic_Directed(g:directed_graph) -> bool:

    visited={}

    for u in g.vertices:
        visited[u]=False    