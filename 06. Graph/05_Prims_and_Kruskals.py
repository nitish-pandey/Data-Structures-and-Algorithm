from graph_implementation import weightedGraph
from disjoint_set import DisjointSet
import heapq
from collections import defaultdict


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._heap)[-1]

    def isEmpty(self):
        return len(self._heap) ==0


# Problem Statement: Find the minimum spanning tree of a graph using Prim's and Kruskal's algorithm

# MST: Minimum Spanning Tree is a subgraph of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.


# 1. Prim's Algorithm

# Algorithm:
# 1. Initialize Priority queue, weight, parent and visited:  Hash-Table
# 2. Set weight of start to zero and push start in the priority queue
# 3. While PQ is not empty, do the follwoing:
#   i. Pop a vertex from PQ and mark it visited
#   ii Iterate over all the adjacent of the vertex and do the following:
#       If the weight of edge betwwen node and its adj is smaller than the weight of hash-table,
#           then update the weight in hash-table,set its parent, and push it to the priority queue
# 4. Initialize Cost to zero and a list to store MST
# 5. Iterate over vertices of Graph
#   If the parent is not -1, add the edge of node and its parent to MST, add the weight to the total-cost




# Time Complexity: O( E + E log V) 
# Space Complexity: O(E) 

def primsMST(G:weightedGraph,start) ->None:

    # Initialize parent,weight and visited

    parent=defaultdict(int)
    weight=defaultdict(int)
    visited=defaultdict(bool)

    for u in G.vertices:
        parent[u]=-1
        weight[u]=1000001
        visited[u]=False

    weight[start]=0
    
    # Initialize Priority Queue
    pq=PriorityQueue()

    pq.push(start,0)

    while not pq.isEmpty():
        u=pq.pop()
        visited[u]=True

        for v in G.getneighbours(u):
            x=G.getWeight(u,v)
            if not visited[v] and  weight[v]>x:
                weight[v]=x
                parent[v]=u
                pq.push(v,x)


    print("\nMST is: ")
    cost=0
    for u in G.vertices:
        if parent[u]!=-1:
            print(parent[u],"--",u)
        cost+=weight[u]

    print("Cost is : ",cost)







# 2. Kruskal's Algorithm

# Algorithm:
# 1. List out all the edges
# 2. Sort all the edges according to weight in ascending order
# 3. Create a empty list for MST, variable cost initialized to zero and A disjoint set
# 4. Iterate over sorted list of edges and do the following:
# 5.    If the both nodes of curr edge is not in same set in disjoint set, then:
# 6.        Add the current edge to the answer
# 7.        Add the weight to the total cost
# 8.        Do the union between the sets of nodes of current edge.



# Time Complexity: O(ElogE) where E is the number of edges
# Space Complexity: O(E) where E is the number of edges


def kruskalsMST(G:weightedGraph)-> None:

    edges=[]

    # Listing all the edges 
    for u in G.vertices:
        for v in G.getneighbours(u):
            if v>u:
                edges.append([u,v,G.getWeight(u,v)])

    # Sorting acc. to weight
    sortedEdges=sorted(edges,key=lambda x:x[2])

    # creating disjoint Set
    ds=DisjointSet()

    mst=[]
    cost=0


    for edge in sortedEdges:
        u,v,w=edge

        # Selecting only the non-cyclic edges
        if not ds.connected(u,v):
            mst.append([u,v])
            ds.union(u,v)
            cost+=w

    print('Cost of MST is: ',cost)
    print("MST is: ", mst)

    return None






def kruskalUsingPQ(G:weightedGraph)-> None:

    # Initializing a PQ
    pq=PriorityQueue()

    # Inserting all the edges into PQ
    for u in G.vertices:
        for v in G.getneighbours(u):
            if v>u:
                pq.push([u,v],G.getWeight(u,v))

    # creating disjoint Set
    ds=DisjointSet()

    mst=[]
    n=len(G.vertices)
    cost=0

    # Iterating Over PQ while MST is incomplete
    while len(mst)<n-1:

        # Extracting the minimum from PQ
        u,v=pq.pop()

        # Selecting only the non-cyclic edges
        if not ds.connected(u,v):
            mst.append([u,v])
            ds.union(u,v)
            cost+=G.getWeight(u,v)

    print('Cost of MST is: ',cost)
    print("MST is: ", mst)

    return None



if __name__=='__main__':

    g=weightedGraph()

    g.addEdge(1,2,2)
    g.addEdge(1,3,3)
    g.addEdge(2,3,1)
    g.addEdge(2,4,3)
    g.addEdge(2,5,2)
    g.addEdge(3,5,1)
    g.addEdge(4,5,5)

    kruskalsMST(g)
    # kruskalUsingPQ(g)

    primsMST(g,1)


