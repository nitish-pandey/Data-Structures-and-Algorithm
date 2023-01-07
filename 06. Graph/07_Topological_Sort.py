from collections import defaultdict
from graph_implementation import directedGraph

# Topological Sort is the linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering.
# Topological sort is only possible in a directed acyclic graph (DAG).

# Topological sort is used in scheduling jobs from the given dependencies among jobs.

# Algorithm:
# 1. Compute in-degree (number of incoming edges) for each of the vertex present in the DAG and initialize the list for answers.
# 2. Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
# 3. Remove a vertex from the queue (Dequeue operation) and then.
# 4. Add the vertex to the list for answer.
# 5. Decrease in-degree by 1 for all its neighboring nodes.
# 6. If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
# 7. Repeat Step 3-6 until the queue is empty.
# 8. Return the answer


# Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
# Space Complexity: O(V)

def topologicalSort(dag:directedGraph) -> list:

    # Step 1
    in_degree=defaultdict(int)

    for u in dag.vertices:
        for v in dag.get_neighbours(u):
            in_degree[v]+=1

    # Step 2
    queue=[]

    for i in dag.vertices:
        if in_degree[i]==0:
            queue.append(i)

    # Step 3
    ans=[]
    while queue:
        u=queue.pop(0)
        ans.append(u)

        # Step 4
        for v in dag.get_neighbours(u):
            in_degree[v]-=1

            # Step 5
            if in_degree[v]==0:
                queue.append(v)

    return ans



def main():

    dag=directedGraph()

    dag.addEdge(1,2)
    dag.addEdge(1,3)
    dag.addEdge(1,4)
    dag.addEdge(2,5)
    dag.addEdge(3,6)
    dag.addEdge(5,6)
    dag.addEdge(6,4)
    dag.addEdge(4,7)

    print(topologicalSort(dag))
    




main()  # Call to main function

# Output:
# [1, 2, 3, 5, 6, 4, 7]