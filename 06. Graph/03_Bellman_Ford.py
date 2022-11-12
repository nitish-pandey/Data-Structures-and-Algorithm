
from graph_implementation import weighted_graph

# Bellman Ford Algorithm is the algorithm to find the shortest path from a source node to all other nodes in a graph.
# It is a greedy algorithm .

# It performs better than Dijkstra's Algorithm in case of graphs with negative edges.
# It is a single source shortest path algorithm.

# Tags: Greedy

# Algorithm:
# 1. Initialize the distance of all nodes to infinity except the source node.
# 2. Relax all the edges V-1 times.
# 3. If there is a negative weight cycle, then the graph has no shortest path.

# Time Complexity: O(VE)
# Space Complexity: O(V)

def bellman_ford(graph, source):
    distance = [float('inf') for _ in range(graph.vertices)]
    distance[source] = 0

    for _ in range(graph.vertices - 1):
        for u in range(graph.vertices):
            for v, w in graph.adjacency_list[u]:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    for u in range(graph.vertices):
        for v, w in graph.adjacency_list[u]:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print('Graph contains negative weight cycle')
                return

    print('Vertex Distance from Source')
    for i in range(graph.vertices):
        print('%d \t\t %d' % (i, distance[i]))






def main():
    graph = weighted_graph(5)
    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)

    print('Graph:')
    graph.print_graph()

    print('Bellman Ford Algorithm:')
    bellman_ford(graph, 0)