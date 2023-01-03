
# AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

# Advantages of AVL Tree over BST:
#   1. AVL trees provide faster lookups than BST because they are more balanced compared to BSTs.
#   2. AVL trees provide faster insertion and deletion operations than BST because they are more balanced compared to BSTs.

# Disadvantages of AVL Tree over BST:
#   1. AVL trees require more memory than BSTs because they store balance factors with each node.
#   2. AVL trees are slower than Red-Black Trees because they may require one or two tree rotations during insertion and deletion.



# Rotations:

#   1. Left Rotation:
#       1.1. Perform a right rotation on the right child of the left child of the node.
#       1.2. Perform a left rotation on the node.

#   2. Right Rotation:
#       2.1. Perform a left rotation on the left child of the right child of the node.
#       2.2. Perform a right rotation on the node.



# Cases:

#   1. Left Left Case:
#       1.1. Perform a right rotation on the node.

#   2. Left Right Case:
#       2.1. Perform a left rotation on the left child of the node.
#       2.2. Perform a right rotation on the node.

#   3. Right Right Case:
#       3.1. Perform a left rotation on the node.

#   4. Right Left Case:
#       4.1. Perform a right rotation on the right child of the node.
#       4.2. Perform a left rotation on the node.



# Time Complexity:
#   1. Insertion: O(log n)
#   2. Deletion: O(log n)
#   3. Search: O(log n)




class AVL:

    class node:
        def __init__(self,d) -> None:
            self.data=d
            self.left=None
            self.right=None
            self.bf=0
            pass

    def __init__(self) -> None:
        self.root=None
        pass

    

