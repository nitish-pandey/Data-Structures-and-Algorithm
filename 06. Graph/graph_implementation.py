from collections import defaultdict


class simpleGraph:

    def __init__(self,n=20) -> None:

        self.__adjList=defaultdict(list)
        self.__adjMatrix=[[False] *n] *n
        self.__vertices=set()

        pass

    def __addVertex(self,u:int) ->None:
        self.__vertices.add(u)


    def addEdge(self,u:int,v:int) -> None:

        self.__addVertex(u)
        self.__addVertex(v)

        self.__adjList[u].append(v)
        self.__adjMatrix[u][v]=True


        # Comment below 2 lines in case of directed graph
        self.__adjList[v].append(u)
        self.__adjMatrix[v][u]=True


    def get_neighbours(self,u:int) -> list:

        return self.__adjList[u]  # This is in the implementation of adjacency list

        # In case of implementation through adjacency matrix

        # ans=[]

        # for i in range(len(self.__adjMatrix[u])):
        #     if self.__adjMatrix[u][i]:
        #         ans.append(i)

        # return ans





class weightedGraph:

    def __init__(self,n=20) -> None:
        self.__adjList=defaultdict(list)
        self.__adjMatrix=[[-1]*n]*n
        self.__vertices=set()
        pass

    def __addVertex(self,u:int):
        self.__vertices.add(u)

    
    def addEdge(self,u:int,v:int,w:int) ->None:

        self.__addVertex(u)
        self.__addVertex(v)

        self.__adjList[u].append([v,w])
        self.__adjMatrix[u][v]=w


        # Comment below 2 lines in case of directed Graph
        self.__adjMatrix[v][u]=w
        self.__adjList[v].append([u,w])


    def getneighbours(self,u:int) ->list:

        return [ a[0] for a in self.__adjList[u]]   # this is for the implementation of Adjacency List

        # In case of implementation through adjacency matrix

        # ans=[]

        # for i in range(len(self.__adjMatrix[u])):
        #     if self.__adjMatrix[u][i]>0:
        #         ans.append(i)

        # return ans

    def getWeight(self,u:int,v:int) ->int:

        # return self.__adjMatrix[u][v]  # This is for the implementation of Adjacency Matrix

        # In case of implementation through adjacency List

        l=self.__adjList[u]

        for pair in l:
            if pair[0]==v:
                return pair[1]

        return -1   



class directedGraph:

    def __init__(self) -> None:

        self.__adjList=defaultdict(list)
        self.vertices=set()

        pass

    def __addVertex(self,u:int) ->None:
        self.vertices.add(u)


    def addEdge(self,u:int,v:int) -> None:

        self.__addVertex(u)
        self.__addVertex(v)

        self.__adjList[u].append(v)

    def get_neighbours(self,u:int) -> list:

        return self.__adjList[u]




def main():

    g=weightedGraph()

    g.addEdge(1,2,5)
    g.addEdge(1,3,4)
    g.addEdge(2,4,7)
    g.addEdge(3,4,9)

    print(g.getWeight(2,1))
            


# main()

