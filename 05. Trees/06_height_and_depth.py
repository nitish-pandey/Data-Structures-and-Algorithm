
from bst import BST


# Problem statement 1: Find the height of a binary tree

# Height of a binary tree is the number of edges in the longest path from the root to a leaf node

# Algorithm:
# if root is None, return 0
# Else, return 1 + max(height(root.left),height(root.right))

# Time Complexity: O(n)
# Space Complexity: O(n)

def height(root):

    if root is None:
        return 0

    a=height(root.left)
    b=height(root.right)

    return 1 + max(a,b)




# Problem statement 2: Find the depth of a node in a binary tree

# Depth of a node is the number of edges in the path from the root to the node

# Algorithm:
# if root is None, return 0
# if root.value == value, return 0
# Else, return 1 + min(depth(root.left,value),depth(root.right,value))


# Time Complexity: O(n)
# Space Complexity: O(n)

def depth(root,value):

    if root is None:
        return 0

    if root.value == value:
        return 0

    a=depth(root.left,value)
    b=depth(root.right,value)

    if a==0 and b==0:
        return 0

    return 1 + min(a,b)





# Problem statement 3: Find the diameter of a binary tree

# Diameter of a tree is the maximum distance between any two nodes in the tree

# Algorithm:
# if root is None, return 0
# Else, return max(height(root.left)+height(root.right)+1,diameter(root.left),diameter(root.right))


# Time Complexity: O(n^2)
# Space Complexity: O(n)

def diameter(root):

    if root is None:
        return 0

    a=height(root.left)+height(root.right)+1
    b=diameter(root.left)
    c=diameter(root.right)

    return max(a,b,c)





def main():

    bst = BST()

    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)

    print("Height of the tree is: ",height(bst.root))
    print("Depth of the node 7 is: ",depth(bst.root,7))
    print("Diameter of the tree is: ",diameter(bst.root))




main() # call main function

# Output:
# Height of the tree is:  3
# Depth of the node 7 is:  1
# Diameter of the tree is:  5
