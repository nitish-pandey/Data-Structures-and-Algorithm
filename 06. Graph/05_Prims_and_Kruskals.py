from graph_implementation import weighted_graph
import heapq
import sys

# You are given a graph with N nodes and M edges. Each edge has a weight associated with it.
# You have to find the minimum spanning tree of the graph.

# Minimum spanning tree is a subset of the graph which has all the nodes covered with the minimum possible total weight of the edges.
# MST is a special case of a tree. It has N nodes and N-1 edges.

# Problem Statement 1: Prims Algorithm

# Tags: Greedy, MST

# Approach: We will select the minimum cost edge from the unvisited nodes and add it to the visited nodes. We will keep doing this until all the nodes are visited.

# Algorithm:
# 1. Create a min heap, parent array and key array.
# 2. For all the vertices, add the vertex and the key as infinity to the min heap and the parent as -1 to the parent array.
# 3. Make the key of the source node as 0 and decrease the key of the source node in the min heap.
# 4. While the min heap is not empty, do the following:
#    a. Pop the node from the min heap.
#    b. For each of the neighbours of the popped node,
#       check if the neighbour is present in the min heap and the key of the neighbour is greater than the weight of the edge between the popped node and the neighbour.
#       If yes, then update the key of the neighbour and the parent of the neighbour and decrease the key of the neighbour in the min heap.
# 5. Return the parent array.

# Time Complexity: O(ElogV)
# Space Complexity: O(V)


def prims(graph:weighted_graph, source:int) -> list:

    min_heap=[]
    parent={}
    key={}

    for vertices in graph.vertices:
        parent[vertices]=-1
        key[vertices]=sys.maxsize
        min_heap.append((sys.maxsize,vertices))

    key[source]=0
    heapq.heapify(min_heap)
    heapq.decrease_key(min_heap,(sys.maxsize,source),(0,source))

    while min_heap:
        popped=heapq.heappop(min_heap)
        popped_node=popped[1]

        for neighbour in graph.get_neighbours(popped_node):

            if neighbour in min_heap and graph.get_weight(popped_node,neighbour)<key[neighbour]:
                key[neighbour]=graph.get_weight(popped_node,neighbour)
                parent[neighbour]=popped_node
                heapq.decrease_key(min_heap,(sys.maxsize,neighbour),(key[neighbour],neighbour))

    return parent


# <--End of Implementation-->


# Problem Statement 2: Kruskals Algorithm

# Tags: Greedy, MST

# Algorithm:
# 1. Create a disjoint set and a result array.
# 2. Sort the edges of the graph in ascending order of their weights.
# 3. For each edge in the sorted edges, do the following:
#    a. If the source and the destination of the edge are not in the same set, then add the edge to the result array and union the source and the destination.  
# 4. Return the result array.


# Time Complexity: O(ElogE)
# Space Complexity: O(E)



def krushkals(graph:weighted_graph) -> list:

    disjoint_set=set()
    result=[]

    sorted_edges=sorted(graph.edges,key=lambda x: x[2])

    for edge in sorted_edges:
        source=edge[0]
        destination=edge[1]
        weight=edge[2]

        if disjoint_set.find(source)!=disjoint_set.find(destination):
            result.append(edge)
            disjoint_set.union(source,destination)

    return result

# <--End of Implementation-->

