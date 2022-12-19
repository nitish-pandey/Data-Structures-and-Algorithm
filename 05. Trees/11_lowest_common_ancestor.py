from bst import BST

# Problem Statement: You are given a Tree and 2 nodes: Return the Lowest Common Ancestor

# LCA is the node which is the lowest in the tree and has both the nodes as its descendants
# For example, in the following tree, the LCA of 4 and 5 is 2, and LCA of 4 and 6 is 1.

#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7


# Algorithm:
# 1. If root is either of two given nodes, return root
# 2. Recursively call function for left-subtree and right-subtree of root
# 3. If Both of the answers are not None, return root
# 4. Return the answer which is not None(NULL)

# Time Complexity: O(n)


def LCA(root,node1,node2):

    if root is None:
        return None

    if root is node1 or root is node2:
        return root

    left_LCA=LCA(root.left,node1,node2)
    right_LCA=LCA(root.right,node1,node2)

    if left_LCA and right_LCA:
        return root

    if left_LCA:
        return left_LCA

    return right_LCA


    
def main():

    tree=BST()
    tree.insert(11)
    tree.insert(12)
    tree.insert(3)
    tree.insert(4)
    tree.insert(15)
    tree.insert(16)
    tree.insert(14)

    node1=tree.root.left
    node2=tree.root.right

    print(LCA(tree.root,node1,node2).value)




main() # Call to main()

# Output:
# 11