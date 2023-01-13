from graph_implementation import weightedGraph

# Problem Statement: Implement Floyd Warshall Algorithm

# Floyd Warshall Algorithm is used to find the shortest path between all the pairs of vertices in a weighted graph.
# Floyd Warshall Algorithm is a dynamic programming algorithm.


# Algorithm:
# 1. Create a distance matrix dist[][] and initialize all entries in it as INFINITE.
# 2. Assign dist[i][i] as 0 for all i.
# 3. For each edge (u, v), assign dist[u][v] as the weight of the edge.
# 4. For each vertex k, do the following:
#     a. For each vertex i, do the following:
#         i. For each vertex j, do the following:
#             1. If dist[i][j] > dist[i][k] + dist[k][j], then update dist[i][j] as dist[i][k] + dist[k][j].
# 5. Print the distance matrix dist[][].

# Time Complexity: O(V^3)
# Space Complexity: O(V^2)


def floyd_warshall(G:weightedGraph):

    # Initialize the distance matrix
    dist={vertex:{} for vertex in G.vertices}

    for u in G.vertices:
        for v in G.vertices:
            dist[u][v]=float('inf')

    for u in G.vertices:
        dist[u][u]=0

    # Assign the weight of the edge
    for u,v,w in G.edges():
        dist[u][v]=w
        dist[v][u]=w


    # Floyd Warshall Algorithm
    for k in G.vertices:
        for i in G.vertices:
            for j in G.vertices:
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]


    # Print the distance matrix
    for u in dist:
        for v in dist[u]:
            print(f"Distance from {u} to {v} is {dist[u][v]}")


    return dist






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


    dist=floyd_warshall(g)



main() # call to main function


# Output:
# Distance from 0 to 0 is 0
# Distance from 0 to 1 is 4
# Distance from 0 to 2 is 12
# Distance from 0 to 3 is 19
# Distance from 0 to 4 is 28
# Distance from 0 to 5 is 16
# Distance from 0 to 7 is 8
# Distance from 0 to 8 is 14
# Distance from 1 to 0 is 4
# Distance from 1 to 1 is 0
# Distance from 1 to 2 is 8
# Distance from 1 to 3 is 15
# Distance from 1 to 4 is 24
# Distance from 1 to 5 is 12
# Distance from 1 to 7 is 11
# Distance from 1 to 8 is 10
# Distance from 2 to 0 is 12
# Distance from 2 to 1 is 8
# Distance from 2 to 2 is 0
# Distance from 2 to 3 is 7
# Distance from 2 to 4 is 16
# Distance from 2 to 5 is 4
# Distance from 2 to 7 is 19
# Distance from 2 to 8 is 2
# Distance from 3 to 0 is 19
# Distance from 3 to 1 is 15
# Distance from 3 to 2 is 7
# Distance from 3 to 3 is 0
# Distance from 3 to 4 is 9
# Distance from 3 to 5 is 11
# Distance from 3 to 7 is 26
# Distance from 3 to 8 is 9
# Distance from 4 to 0 is 28
# Distance from 4 to 1 is 24
# Distance from 4 to 2 is 16
# Distance from 4 to 3 is 9
# Distance from 4 to 4 is 0
# Distance from 4 to 5 is 20
# Distance from 4 to 7 is 35
# Distance from 4 to 8 is 18
# Distance from 5 to 0 is 16
# Distance from 5 to 1 is 12
# Distance from 5 to 2 is 4
# Distance from 5 to 3 is 11
# Distance from 5 to 4 is 20
# Distance from 5 to 5 is 0
# Distance from 5 to 7 is 23
# Distance from 5 to 8 is 6
# Distance from 7 to 0 is 8
# Distance from 7 to 1 is 11
# Distance from 7 to 2 is 19
# Distance from 7 to 3 is 26
# Distance from 7 to 4 is 35
# Distance from 7 to 5 is 23
# Distance from 7 to 7 is 0
# Distance from 7 to 8 is 21
# Distance from 8 to 0 is 14
# Distance from 8 to 1 is 10
# Distance from 8 to 2 is 2
# Distance from 8 to 3 is 9
# Distance from 8 to 4 is 18
# Distance from 8 to 5 is 6
# Distance from 8 to 7 is 21
# Distance from 8 to 8 is 0