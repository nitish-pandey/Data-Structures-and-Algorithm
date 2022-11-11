from graph_implementation import weighted_graph


# You are given a graph with N nodes and M edges. Each edge has a weight associated with it.
# You have to find the minimum spanning tree of the graph.

# Minimum spanning tree is a subset of the graph which has all the nodes covered with the minimum possible total weight of the edges.
# MST is a special case of a tree. It has N nodes and N-1 edges.

# Problem Statement 1: Prims Algorithm

# Tags: Greedy, MST

# Approach: We will select the minimum cost edge from the unvisited nodes and add it to the visited nodes. We will keep doing this until all the nodes are visited.

# Algorithm:
# 1. Select the node with the minimum cost edge and add it to the visited nodes.
# 2. Add the cost of the edge to the total cost.
# 3. Repeat the above steps until all the nodes are visited.

# Time Complexity: O(N^2)
# Space Complexity: O(N)



# <--End of Implementation-->


# Problem Statement 2: Kruskals Algorithm

# Tags: Greedy, MST

# Algorithm:
# 1. Create min heap of all the edges.
# 2. Select the edge with the minimum cost and add it to the visited edges.
# 3. Repeat the above steps until all the nodes are visited.

# Time Complexity: O(ElogE)
# Space Complexity: O(E)
