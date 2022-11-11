
from graph_implementation import weighted_graph

# Problem Statement: Floyd Warshal Algorithm
# Floyd Warshal Algorithm is the algorithm to find the shortest path between all pairs of nodes in a graph.
# It is a dynamic programming algorithm.

# It is a all pairs shortest path algorithm.

# Tags: Dynamic Programming

# Algorithm:
# 1. Create a distance matrix and initialize it with infinity.
# 2. Set the distance of the node to itself as 0.
# 3. For all the edges, set the distance of the edge as the weight of the edge.
# 4. For all the nodes, set the distance of the node to the adjacent node as the weight of the edge.
# 5. For all the nodes, set the distance of the node to the node through the adjacent node as the distance of the node to the adjacent node + distance of the adjacent node to the node.
# 6. Repeat step 5 until all the nodes are visited.

# Time Complexity: O(V^3)
# Space Complexity: O(V^2)

# Implementation:

