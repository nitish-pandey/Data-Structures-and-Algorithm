
import heapq
import sys
from graph_implementation import weighted_graph


# Problem Statement: Dijkstra Algorithm

# Dijkstra Algorithm is the algorithm to find the shortest path from a source node to all other nodes in a graph.
# It is a greedy algorithm and it uses a priority queue to find the shortest path.

# It is a single source shortest path algorithm.

# Tags: Greedy


# Algorithm:
# 1. Create a dist array/dict and initialize all the distances to infinity except the source node which is 0.
# 2. Create a min heap and push the source node with distance 0.
# 3. While the min heap is not empty, do the following:
#    a. Pop the node from the min heap.
#    b. For each of the neighbours of the popped node, 
#       check if the distance of the neighbour is greater than the distance of the popped node + the weight of the edge between the popped node and the neighbour.
#       If yes, then update the distance of the neighbour and push the neighbour into the min heap.
# 4. Return the dist array.


# Time Complexity: O(ElogV)
# Space Complexity: O(V)


# Implementation:

def dijkstra(graph:weighted_graph, source:int) -> list:

    dist={}

    for vertices in graph.vertices:
        dist[vertices]=sys.maxsize

    dist[source]=0

    min_heap=[]
    heapq.heappush(min_heap,(0,source))

    while min_heap:
        popped=heapq.heappop(min_heap)
        popped_node=popped[1]

        for neighbour in graph.get_neighbours(popped_node):

            curr_dist=dist[popped_node]+graph.get_weight(popped_node,neighbour)

            if curr_dist<dist[neighbour]:
                dist[neighbour]=curr_dist
                heapq.heappush(min_heap,(curr_dist,neighbour))

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


main() # calling main function

# Output:
# {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}