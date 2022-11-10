
import heapq
import sys
from graph_implementation import simple_graph


# Problem Statement: Dijkstra Algorithm

# Dijkstra Algorithm is the algorithm to find the shortest path from a source node to all other nodes in a graph.
# It is a greedy algorithm and it uses a priority queue to find the shortest path.
# It is a single source shortest path algorithm.


# Algorithm:
# 1. Create a priority queue Q.
# 2. Create a distance array dist[] and initialize all distances as infinite except dist[src] where src is the source vertex.
# 3. While Q is not empty, do the following:
#     a. Extract the vertex u with the minimum distance value from Q.
#     b. Loop through all adjacent vertices of u and do the following:
#         i. If there is a shorter path to v through u, then update the distance value of v in dist[].
#         ii. If v is not in Q, then insert v into Q with its distance value.
#        iii. If v is in Q, then update its distance value in Q.
# 4. Print the distance array dist[] to get the shortest paths from src to all other vertices.


# Time Complexity: O(ElogV)
# Space Complexity: O(V)


# Implementation:

def dijkstra(graph, source):

    dist = {vertex: sys.maxsize for vertex in graph.vertices}
    dist[source] = 0

    pq = [(0, source)]

    while len(pq) > 0:

        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > dist[current_vertex]:
            continue

        for neighbor in graph.edges[current_vertex]:

            distance = current_distance + graph.edges[current_vertex][neighbor]

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist



# <--End of Implementation-->

