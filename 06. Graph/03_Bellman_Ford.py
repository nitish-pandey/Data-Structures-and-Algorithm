
from graph_implementation import weighted_graph
import sys

# Bellman Ford Algorithm is the algorithm to find the shortest path from a source node to all other nodes in a graph.
# It is a greedy algorithm .

# It performs better than Dijkstra's Algorithm in case of graphs with negative edges.
# It is a single source shortest path algorithm.

# Tags: Greedy

# Algorithm:
# 1. Initialize the distance of all the nodes to infinity except the source node which is 0.
# 2. Initialize the parent of all the nodes to None.
# 3. For the number of vertices - 1 times, do the relaxation of all the edges.
# 4. For each of the edges, check if the distance of the destination node is greater than the distance of the source node + the weight of the edge.
#   If yes, then update the distance of the destination node and update the parent of the destination node to the source node.
# 5. After the above step, check if the distance of the destination node is greater than the distance of the source node + the weight of the edge.
#   If yes, then there is a negative weight cycle in the graph.
# 6. Return the dist and parent array.

# Time Complexity: O(VE)
# Space Complexity: O(V)


def relaxation(u, v, w, dist, parent):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u

def bellman_ford(graph: weighted_graph, source: int):

    dist={}
    parent={}

    for i in graph.vertices:
        dist[i]=sys.maxsize
        parent[i]=None

    dist[source]=0

    for i in range(len(graph.vertices)-1):
        for u in graph.vertices:
            for v in graph.get_neighbours(u):
                relaxation(u,v,graph.get_weight(u,v),dist,parent)


    for u in graph.vertices:
        for v in graph.get_neighbours(u):
            if dist[v]>dist[u]+graph.get_weight(u,v):
                print('Negative Weight Cycle')
                

    print('Distance:',dist)
    print('Parent:',parent)





def main():
    graph = weighted_graph()
    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)

    print('Graph:')
    print('Bellman Ford Algorithm:')
    bellman_ford(graph, 0)


main() # call main function

# Output:

# Distance: {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
# Parent: {0: None, 1: 0, 2: 1, 3: 1, 4: 1}