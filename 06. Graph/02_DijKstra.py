
import heapq
import sys
from graph_implementation import weighted_graph


# Problem Statement: Dijkstra Algorithm

# Dijkstra Algorithm is the algorithm to find the shortest path from a source node to all other nodes in a graph.
# It is a greedy algorithm and it uses a priority queue to find the shortest path.

# It is a single source shortest path algorithm.

# Tags: Greedy


# Algorithm:
# 1. Create a min heap and initialize all the distances to infinity.
# 2. Set the distance of the source node to 0.
# 3. While the heap is not empty, pop the node with the minimum distance.
# 4. For all the adjacent nodes of the popped node, update the distance if the distance of the popped node + weight of the edge between the popped node and the adjacent node is less than the distance of the adjacent node.
# 5. Repeat step 3 and 4 until the heap is empty.
# 6. Return the distance array.


# Time Complexity: O(ElogV)
# Space Complexity: O(V)


# Implementation:

def dijkstra(graph:weighted_graph, source:int) -> list:

    dist={}

    min_heap=[]

    for vertices in graph.vertices:
        dist[vertices]=sys.maxsize
        heapq.heappush(min_heap,(dist[vertices],vertices))

    dist[source]=0
    # print(min_heap)


    while min_heap:

        popped=heapq.heappop(min_heap)
        popped=popped[1]

        for adj,cost in graph.get_neighbours(popped):
            
            if dist[popped]+cost<dist[adj]:
                dist[adj]=dist[popped]+cost
                heapq.heappush(min_heap,(dist[adj],adj))

    return dist




# <--End of Implementation-->



def main():

    g=weighted_graph()

    g.add_edge(0,1,4)
    g.add_edge(0,7,8)
    g.add_edge(1,2,8)   
    g.add_edge(1,7,11)
    g.add_edge(2,3,7)
    g.add_edge(2,8,2)
    g.add_edge(2,5,4)
    g.add_edge(3,4,9)
    g.add_edge(3,5,14)

    print(dijkstra(g,0))


main()