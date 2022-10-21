from collections import defaultdict

class simple_graph:

    def __init__(self):

        self.edges=defaultdict(list)
        self.vertices=set()


    def add_edge(self,u,v):

        self.edges[u].append(v)
        self.edges[v].append(u)
        self.vertices.add(u)
        self.vertices.add(v)

