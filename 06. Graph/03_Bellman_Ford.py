from graph_implementation import weightedGraph

# Problem Statement: Implement Bellman Ford

# Bellman ford is the single source shortest Path algorithm like Dijkstra.
# It also works with negative edges.

# Algorithm:
# 1. Initialize the distance of all the nodes to infinity and parent to NULL.
# 2. Initialize the distance of source node to 0.
# 3. Relax all the edges V-1 times.
# 4. If there is a negative cycle, then the graph is not a DAG.
# 5. If there is no negative cycle, then the graph is a DAG.
# 


# Time Complexity: O(V*E)
# Space Complexity: O(V)


def BellmanFord(G:weightedGraph,src:int) :
    dist={vertex:float('inf') for vertex in G.vertices}
    parent={vertex:None for vertex in G.vertices}

    dist[src]=0

    for i in range(len(G.vertices)-1) :
        for u,v,w in G.edges() :
            if dist[u]+w<dist[v] :
                dist[v]=dist[u]+w
                parent[v]=u

    for u,v,w in G.edges() :
        if dist[u]+w<dist[v] :
            print("Negative Cycle")
            return [],[]
    

    for u in dist:
        print(f"Distance to {u} is {dist[u]}")

    return dist,parent


def printPath(src,dest,parent)->None:
    if src==dest:
        print(src,end='->')
        return

    printPath(src,parent[dest],parent)
    print(dest,end='->')



def main():

    g=weightedGraph()
    g.addEdge(0,1,4)
    g.addEdge(0,7,8)
    g.addEdge(1,2,8)
    g.addEdge(1,7,11)
    g.addEdge(2,3,7)
    g.addEdge(2,8,2)
    g.addEdge(2,5,4)
    g.addEdge(3,4,9)
    g.addEdge(3,5,14)


    dist,parent=BellmanFord(g,0)

    printPath(0,8,parent)
    print()



main() # call to main function

# Output:
# Distance to 0 is 0
# Distance to 1 is 4
# Distance to 2 is 12
# Distance to 3 is 19
# Distance to 4 is 28
# Distance to 5 is 16
# Distance to 7 is 8
# Distance to 8 is 14

# 0->1->2->8->
