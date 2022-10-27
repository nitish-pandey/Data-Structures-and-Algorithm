

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

# Algorithm:
# 1. If both trees are empty, return true
# 2. Else if any of the tree is empty, return false
# 3. Check if the root of both trees are equal, if not return false
# 4. Call recursively for the left subtree of the first tree and right subtree of the second tree
# 5. Call recursively for the right subtree of the first tree and left subtree of the second tree
# 6. Return true if both the above calls return true, else return false

# Time Complexity: O(n)
# Space Complexity: O(n)

def isMirror(root1,root2):

    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.value != root2.value:
        return False

    return isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)





# Problem statement 4: Check if a binary tree is a symmetric tree
# Symmetric tree is a tree where the left subtree is a mirror image of the right subtree


# Algorithm:
# 1. Return the result of the isMirror function passing the root of the tree as the both argument

# Time Complexity: O(n)
# Space Complexity: O(n)

def isSymmetric(root):

    return isMirror(root,root)



# Problem statement 5: Check if a binary tree is balanced or not

# Algorithm:
# 1. If the tree is empty, return true
# 2. Get the height of the left subtree
# 3. Get the height of the right subtree
# 4. If the difference between the height of the left and right subtree is greater than 1, return false
# 5. Else, return the result of the isBalanced function passing the left subtree and right subtree as the argument

# Time Complexity: O(n^2)
# Space Complexity: O(n)


def getHeight(root):

    if root is None:
        return 0

    return 1+max(getHeight(root.left),getHeight(root.right))




def isBalanced(root):

    if root is None:
        return True

    lh=getHeight(root.left)
    rh=getHeight(root.right)

    if abs(lh-rh) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)



# Problem statement 6: Check if a binary tree is a binary search tree or not

# Algorithm:
# 1. If the tree is empty, return true
# 2. If the left subtree is not empty, check if the root is greater than the maximum value in the left subtree, if not return false
# 3. If the right subtree is not empty, check if the root is less than the minimum value in the right subtree, if not return false
# 4. Else, return the result of the isBST function passing the left subtree and right subtree as the argument

# Time Complexity: O(n^2)
# Space Complexity: O(n)

def maxValue(root):

    if root is None:
        return float('-inf')

    return max(root.value,maxValue(root.left),maxValue(root.right))


def minValue(root):

    if root is None:
        return float('inf')

    return min(root.value,minValue(root.left),minValue(root.right))



def isBST(root):

    if root is None:
        return True

    if root.left is not None and maxValue(root.left) > root.value:
        return False

    if root.right is not None and minValue(root.right) < root.value:
        return False

    return isBST(root.left) and isBST(root.right)





#  check for complete, full, perfect, balanced, degenerate, and skewed binary trees



