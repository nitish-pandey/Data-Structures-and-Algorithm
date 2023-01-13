from graph_implementation import simpleGraph
from disjoint_set import DisjointSet

# Problem Statement: Detect Cycle in given graph: Undirected

# 1. Using modified DFS/BFS

# Approach: 
# Use the BFS/DFS traversal, if the node is encountered again and it is not parent node, then cycle is present

# Time Complexity: O(V + E)
# Space Comlpexity: O(V)

def detectCycle_DFS(G:simpleGraph) ->bool:

    visited=dict()
    parent=dict()

    for u in G.vertices:
        visited[u]=False
        parent[u]=-1


    def DFS(node):
        visited[node]=True

        for u in G.get_neighbours(node):

            if not visited[u]:
                parent[u]=node
                if DFS(u):
                    return True
            
            elif parent[node] != u:
                return True

        return False


    for u in G.vertices:
        if not visited[u]:
            if DFS(u):
                return True

    return False


    




# 2. Using Disjoint Set

# Approach:
# Create a disjoint Set
# For all the edges:
#   If 2 vertices are in same set, cycle is present-> return True
#   Else, do the union of 2 vertices
# Return False 

# Time Complexity: O( E )
# Space Complexity: O( V)


def detectCycle_DisjointSet(G:simpleGraph) ->bool:

    ds=DisjointSet()

    for u in G.vertices:
        for v in G.get_neighbours(u):
            if v>=u:
                if ds.connected(u,v):
                    return True
                ds.union(u,v)

    return False




