

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


# Algorithm to check if one binary tree is subset of another:
# 1. Check if the two trees are identical
# 2. If not, check if the left subtree of the first tree is a subtree of the second tree
# 3. If not, check if the right subtree of the first tree is a subtree of the second tree
# 4. If not, return false

# Time Complexity: O(n)
# Space Complexity: O(n)

def check_if_subtree(root1,root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None:
        return False

    if root2 is None:
        return True

    ans=check_if_identical(root1,root2)

    return check_if_subtree(root1.left,root2) or check_if_subtree(root1.right,root2) or ans



# Problem statement 3: Check if a binary tree is a mirror of another binary tree
# Mirror of a binary tree is a tree in which left and right subtrees are interchanged

# To be Updated:




# Problem statement 4: Check if a binary tree is a symmetric tree
# Symmetric tree is a tree where the left subtree is a mirror image of the right subtree





#  check for complete, full, perfect, balanced, degenerate, and skewed binary trees



