from graph_implementation import simple_graph


# Problem Statement: Implement BFS and DFS for a graph.

# BFS ( Breadth First Search ):: is a graph traversal algorithm that starts traversing the graph from root node and explores all the neighbouring nodes. 
#       Then, it selects the nearest node and explore all the unexplored nodes. 
#       The algorithm follows the same process for each of the nearest node until it finds the goal.
# Data Structure used: Queue


# Algorithm: BFS
# 1. Create a queue and enqueue the root node.
# 2. Mark the root node as visited.
# 3. While the queue is not empty:
#     1. Dequeue a node from the queue.
#     2. Print the node.
#     3. For each of the adjacent of the dequeued node:
#         1. If the adjacent is not visited:
#             1. Mark the adjacent as visited.
#             2. Enqueue the adjacent.



# Time Complexity: O(V+E)
# Space Complexity: O(V)




def BFS(graph,start):

    if start not in graph.edges:
        return

    queue=[start]
    visited=set()
    visited.add(start)

    while queue:

        curr=queue.pop(0)
        print(curr,end=" -> ")

        for adjacent in graph.edges[curr]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)

    print()





# DFS ( Depth First Search ):: is a graph traversal algorithm that starts traversing the graph from root node and explores as far as possible along each branch before backtracking.
#       The algorithm follows the same process for each of the nearest node until it finds the goal.
# Data Structure used: Stack




# Algorithm: DFS without recursion

# 1. Create a stack and push the root node.
# 2. Mark the root node as visited.
# 3. While the stack is not empty:
#     1. Pop a node from the stack.
#     2. Print the node.
#     3. For each of the adjacent of the popped node:
#         1. If the adjacent is not visited:
#             1. Mark the adjacent as visited.
#             2. Push the adjacent.



def DFS_without_recursion(graph,start):

    if start not in graph.vertices:
        return

    stack=[start]

    visited=set()
    visited.add(start)

    while stack:
        curr=stack.pop()
        print(curr,end="->  ")

        for adjacent in graph.edges[curr]:
            if adjacent not in visited:
                visited.add(adjacent)
                stack.append(adjacent)
    


# Algorithm: DFS using recursion
# 1. Mark the current node as visited.
# 2. Print the current node.
# 3. For each of the adjacent of the current node:
#     1. If the adjacent is not visited:
#         1. Recursively call the DFS function with the adjacent as the current node.



def DFS_using_recursion(graph,start,visited=set()):

    if  start not in graph.vertices:
        return

    print(start,end=" -> ")
    visited.add(start)

    for adjacent in graph.edges[start]:
        if adjacent not in visited:
            DFS_using_recursion(graph,adjacent,visited)

    

def main():

    grph=simple_graph()

    grph.add_edge(1,2)
    grph.add_edge(1,3)
    grph.add_edge(2,4)
    grph.add_edge(2,5)
    grph.add_edge(3,6)
    grph.add_edge(3,5)

    print("\nThe BFS traversal of Graph from 1 is : ")

    BFS(grph,1)
    print()

    print("The DFS traversal of graph without recursion from 1 is: ")

    DFS_without_recursion(grph,1)
    print('\n')

    print("The DFS traversal of graph using recursion from 1 is: ")

    DFS_using_recursion(grph,1)
    print('\n')

        
    
main()

# Output:

# The BFS traversal of Graph from 1 is : 
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 

# The DFS traversal of graph without recursion from 1 is: 
# 1->  3->  5->  6->  2->  4->  

# The DFS traversal of graph using recursion from 1 is: 
# 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 


# Note: The Output of DFS with and without recusion are different. But Both of them are correct.
