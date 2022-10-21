

# Data Structure Implementation: Red Black Tree

# Red Black Tree is a self-balancing Binary Search Tree (BST) where every node follows following rules.

# 1) Every node has a color either red or black.
# 2) Root of tree is always black.
# 3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).
# 4) Every path from a node (including root) to any of its descendant NULL node has the same number of black nodes.

# Time Complexity: O(log n) for insertion, deletion and search operations.
# Space Complexity: O(n) for storing the tree.


class red_black_tree:

    class node:
        def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None
            self.color=1

        

    def __init__(self) -> None:
        self.root=None
        pass

