
from graph_implementation import simpleGraph

# BFS

# Algorithm:
# 1. Create a empty queue
# 2. Push the source node and mark it as visited
# 3. While queue is not empty
# 4. Pop the node from the queue
# 5. Print the node
# 6. For each neighbour of the node
# 7. If not visited, push it to the queue and mark it as visited
# 

# Time Complexity: O(V+E) for Adj-List and O(V^2) for Adj-Matrix 
# Space Complexity: O(V) 



# DFS

# Algorithm:
# 1. Mark the source node as visited and print it
# 2. For each neighbour of the node
# 3. If not visited, recursively call the function with the neighbour as the source node

# Time Complexity: O(V+E) for Adj-List and O(V^2) for Adj-Matrix 
# Space Complexity: O(V) 


class GraphTraversals:

    def __init__(self,graph:simpleGraph) -> None:
        self.G=graph
        self.visited=dict()
        self.parent=dict()
        pass


    def __reset(self):
        for u in self.G.vertices:
            self.visited[u]=False
            self.parent[u]=-1


    def __BFS(self,src:int):

        queue=[]

        queue.append(src)
        self.visited[src]=True

        while queue:

            u=queue.pop(0)
            print(u,end=' ')

            for v in self.G.get_neighbours(u):

                if not self.visited[v]:
                    self.parent[v]=u
                    queue.append(v)
                    self.visited[v]=True



    def BFS(self):

        self.__reset()
        print("BFS: ")

        for u in self.G.vertices:

            if not self.visited[u]:
                self.__BFS(u)
                print()

        self.__reset()
        print()



    def __DFS(self,src:int):

        print(src,end=' ')
        self.visited[src]=True

        for v in self.G.get_neighbours(src):
            if not self.visited[v]:
                self.__DFS(v)
                self.parent[v]=src


    def DFS(self):

        self.__reset()
        print("DFS:")

        for u in self.G.vertices:

            if not self.visited[u]:
                self.__DFS(u)
                print()


        print()







def main():

    g=simpleGraph()

    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(3,2)
    g.addEdge(4,2)
    g.addEdge(3,5)

    g.addEdge(9,10)
    g.addEdge(6,7)
    g.addEdge(7,8)
    g.addEdge(6,9)
    g.addEdge(8,10)

    t=GraphTraversals(g)

    t.BFS()
    t.DFS()



main() # Call to main()
    

# Output:

# BFS: 
# 1 2 3 4 5 
# 6 7 9 8 10 

# DFS:
# 1 2 3 5 4 
# 6 7 8 10 9 