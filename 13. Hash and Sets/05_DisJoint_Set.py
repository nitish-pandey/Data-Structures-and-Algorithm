
# Problem Statement: Implement the Disjoint Set

# Disjoint Set is the collection of sets which are disjoint from each other i.e. they do not have any common element.
# The Disjoint Set is implemented using the concept of trees or forest.

# Operations:
# 1. MakeSet(x): Creates a new set with only one element x.
# 2. Union(x, y): Unites the set that contains x and the set that contains y into a new set that is the union of these two sets.
# 3. Find(x): Returns the representative element of the set that contains x.


class Disjoint_set:

    def __init__(self,n=100) -> None:
        self.parent=[-1 for i in range(n)]
        self.rank=[0]*n
        pass

    def make_set(self,n):
        if self.parent[n]==-1:
            self.parent[n]=n
            self.rank[n]=1

    def find(self,n):

        self.make_set(n)   # comment this line to manually use make-set operation

        if self.parent[n]!=n:
            self.parent[n]=self.find(self.parent[n])

        return self.parent[n]

    def union(self,x,y):

        a=self.find(x)
        b=self.find(y)

        if a==b:
            return
        

        if self.rank[a]>=self.rank[b]:
            self.parent[b]=a
            self.rank[a]+=self.rank[b]

        else:
            self.parent[a]=b
            self.rank[b]+=self.rank[a]


def main():

    ds = Disjoint_set(10)

    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(7, 8)
    ds.union(8, 9)
    ds.union(0, 9)

    print(ds.parent)
    print(ds.rank)




main() # Calling the main function

# Output:
# [6, 0, 0, 3, 3, 3, 6, 6, 6, 6]
# [3, 1, 1, 3, 1, 1, 7, 1, 1, 1]
