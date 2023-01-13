from graph_implementation import weightedGraph
from queue import PriorityQueue

# Problem Statement: Implement Disjkstra Algorithm

# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. 
# It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

# Dijkstra's algorithm is very similar to Prim's algorithm for minimum spanning trees.
# Like Prim's algorithm, it operates by building up a set of vertices S,
# whose final result will form a shortest path tree.
# Unlike Prim's algorithm, which finds the minimum spanning tree, Dijkstra's algorithm finds the shortest path tree.

# Note: Dijkstra's algorithm is not suitable for graphs with negative edge weights,

# Algorithm:
# 1. Initialize the distance of all vertices to infinity except the source vertex which is set to zero.
# 2. Create a priority queue and insert the source vertex into it.
# 3. While the priority queue is not empty, repeat the following steps( 4 and 5 ):
# 4. Remove the vertex with the minimum distance from the priority queue.
# 5. For each neighbor of the vertex removed in step 4, 
#    Do the relaxation and push the neighbor into the priority queue.
# 6. Print/Return the distances at the last

# Time Complexity: O(V + ElogV)
# Space Complexity: O(V)


def dijkstra(G:weightedGraph,start:int)->None:

    dist={vertex:float('inf') for vertex in G.vertices}
    parent={vertex:None for vertex in G.vertices}

    dist[start]=0

    q=PriorityQueue()
    q.put([0,start])

    while not q.empty():
        _,u=q.get()
        for v in G.getneighbours(u):
            if dist[v]>dist[u]+G.getWeight(u,v):
                dist[v]=dist[u]+G.getWeight(u,v)
                parent[v]=u
                q.put([dist[v],v])
    

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


    dist,parent=dijkstra(g,0)

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
