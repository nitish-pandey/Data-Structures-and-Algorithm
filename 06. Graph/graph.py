
class undirected_graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def get_vertices(self):

        return self.graph.keys()


    

class directed_graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def get_vertices(self):

        return self.graph.keys()


    

class weighted_graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append((vertex2, weight))
            self.graph[vertex2].append((vertex1, weight))

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def get_vertices(self):

        return self.graph.keys()

