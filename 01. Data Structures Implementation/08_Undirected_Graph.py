

class graph:

    def __init__(self, V=1000):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, v, w):
        if v>=self.V or w>=self.V:
            return
        
        self.adj[v].append(w)
        self.adj[w].append(v)

    def printGraph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            for node in self.adj[i]:
                print(" -> {}".format(node), end="")
            print()

    def bfs(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.adj[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, s):
        visited = [False] * self.V
        self.__dfs(s, visited)
    
    def __dfs(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        for i in self.adj[s]:
            if visited[i] == False:
                self.__dfs(i, visited)
    