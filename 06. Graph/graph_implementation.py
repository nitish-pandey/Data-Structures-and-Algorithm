from collections import defaultdict
import sys

class simple_graph:

    def __init__(self):

        self.edges=defaultdict(list)
        self.vertices=set()


    def add_edge(self,u,v):

        self.edges[u].append(v)
        self.edges[v].append(u)
        self.vertices.add(u)
        self.vertices.add(v)

    def get_neighbour(self,u):
        if u not in self.vertices:
            return []

        return self.edges[u]



class weighted_graph:

    def __init__(self) -> None:
        self.edges=defaultdict(list)
        self.vertices=set()
        pass


    def add_edge(self,u,v,w):

        self.edges[u].append((v,w))
        self.edges[v].append((u,w))
        self.vertices.add(u)
        self.vertices.add(v)

    def get_neighbours(self,u):
        if u not in self.vertices:
            return []

        edges=[x[0] for x in self.edges[u]]

        return edges

    def get_weight(self,u,v):
        if u not in self.vertices or v not in self.vertices:
            return sys.maxsize

        for adj,cost in self.edges[u]:
            if adj==v:
                return cost

        return sys.maxsize





class directed_graph:

    def __init__(self) -> None:
        self.edges=defaultdict(list)
        self.vertices=set()
        pass

    def add_edge(self,u,v):

        self.edges[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)


    def get_neighbours(self,u):
        if u not in self.vertices:
            return []

        return self.edges[u]
    

    