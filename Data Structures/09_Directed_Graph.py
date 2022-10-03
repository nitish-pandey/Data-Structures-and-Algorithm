
class Graph:

    def __init__(self) -> None:
        self.nodes=set()
        self.adjList=[[]]*1000
        pass

    def insert_node(self,a):
        self.nodes.add(a)

    def insert_edges(self,a,b,c=1):
        if a>=1000 or b>=1000:
            return

        self.insert_node(a)
        self.insert_edges(b)

        