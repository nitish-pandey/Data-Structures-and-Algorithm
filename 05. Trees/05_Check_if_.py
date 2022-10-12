

from bst import BST

# Table of Contents

# 1. Check if two trees are identical
# 2. Check if a tree is a subtree of another tree
# 3. Check if two trees are mirror images of each other
# 4. Check if a tree is symmetric
# 5. Check if the tree is balanced
# 6. Check if the tree is a binary search tree
# 7. Check if the tree is a complete binary tree
# 8. Check if the tree is a perfect binary tree
# 9. Check if the tree is a degenerate binary tree
# 10. Check if the tree is a full binary tree
# 11. Check if the tree is a proper binary tree
# 12. Check if the tree is a skewed binary tree
# 13. Check if the tree is a sum tree
# 14. Check if the tree is a heap
# 15. Check if the tree is a min heap
# 16. Check if the tree is a max heap
# 17. Check if the tree is a min max heap

# Problem Staement 1: Check if two trees are identical or not using recursion


# Algorithm:
# if two root are not equal, return false
# Else, check recursively for the left and right subtrees and return true if both are true

# Time Complexity: O(n)
# Space Complexity: O(n)

def check_if_identical(root1,root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.value != root2.value:
        return False

    return check_if_identical(root1.left,root2.left) and check_if_identical(root1.right,root2.right)



# Problem statement 2: Check if a binary tree is a subtree of another binary tree




def check_if_subtree(root1,root2):

    if root1 is None:
        return False

    if root1.value == root2.value:
        return check_if_identical(root1,root2)

    return check_if_subtree(root1.left,root2) or check_if_subtree(root1.right,root2)



# Problem statement 3: Check if a binary tree is a mirror of another binary tree

# Algorithm:
# if two root are not equal, return false
# Else, check recursively for the left and right subtrees and return true if both are true


def check_if_mirror(root1,root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.value != root2.value:
        return False

    return check_if_mirror(root1.left,root2.right) and check_if_mirror(root1.right,root2.left)




# Problem statement 4: Check if a binary tree is a symmetric tree


def check_if_symmetric(root):

    if root is None:
        return True

    if not root.left and not root.right:
        return True

    if not root.left or not root.right:
        return False

    if root.left.value != root.right.value:
        return False

    return check_if_symmetric(root.left) and check_if_symmetric(root.right)



#  check for complete, full, perfect, balanced, degenerate, and skewed binary trees



