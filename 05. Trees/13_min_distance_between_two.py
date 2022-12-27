
# Problem Statement: You are given a Binary Tree and 2 nodes. You have to return the distance between these nodes.

# Distance between two nodes is the minimum number of edges between them.

# Algorithm:
# 1. Find out the LCA ( refer to Code no. 11)
# 2. Find the depth of node1 and node2 from lca 
# 3. return the sum of distance

def LCA(root,node1,node2):
    if not root:
        return None
    
    if root is node1 or root is node2:
        return root

    left=LCA(root.left,node1,node2)
    right=LCA(root.right,node1,node2)

    if left and right:
        return root

    if left:
        return left

    return right



def depth(root,node):
    if root is None:
        return 100000000

    if root is node:
        return 0

    l=depth(root.left,node)
    r=depth(root.right,node)

    return min(l,r)+1



def min_distance(root,node1,node2):

    lca=LCA(root,node1,node2)

    d1=depth(lca,node1)
    d2=depth(lca,node2)

    return d1+d2