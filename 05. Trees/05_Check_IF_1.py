

from bst import BST

# Table of Contents: Part 1

# 1. Check if two trees are identical
# 2. Check if a tree is a subtree of another tree
# 3. Check if two trees are mirror images of each other
# 4. Check if a tree is symmetric
# 5. Check if the tree is balanced
# 6. Check if the tree is a binary search tree


# Problem Staement 1: Check if two trees are identical or not using recursion


# Algorithm:
# if two root are not equal, return false
# Else, check recursively for the left and right subtrees and return true if both are true
# Base case: if both the roots are null, return true

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


# <End of Problem Statement 1>


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


# <End of Problem Statement 2>



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



# Problem statement 5: Check if a binary tree is balanced or not in O(n) time

# Algorithm:
# 1. If the tree is empty, return true
# 2. Create two variables to store the height of the left and right subtree
# 3. Call the isBalanced function recursively for the left subtree and store the result in lh
# 4. Call the isBalanced function recursively for the right subtree and store the result in rh
# 5. Store the maximum of lh and rh in the height variable + 1
# 6. Return true if the difference between lh and rh is less than 2, else return false


# Time Complexity: O(n)
# Space Complexity: O(n)


def isBalanced(root,height=0):

    if root is None:
        return True

    lh=0
    rh=0

    if isBalanced(root.left,lh) is False:
        return False

    if isBalanced(root.right,rh) is False:
        return False

    height=max(lh,rh)+1

    return abs(lh-rh)<2



# <End of Problem Statement 5>


# Problem statement 6: Check if a binary tree is a binary search tree or not