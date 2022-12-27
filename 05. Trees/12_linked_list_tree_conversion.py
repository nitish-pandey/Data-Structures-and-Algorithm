from bst import *

# Problem Statement: You are given a Binary Tree. You have to flatten the Tree.
# Flatten means you have to convert the tree into a linked list.
# The left child of every node should be None and right child should contain the next node in the preorder traversal.

# Sample Input Tree:
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6

# Sample Output Tree:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Algorithm:
# 1. Recursively flatten for the left and right subtree
# 2. If left subtree is null, return
# 3. Store the left tail
# 4. Set  right of left tail = right of root
# 5.Set right of root =left of root
# 6. set left of root as NULL


def flatten(root:node):

    if not root or (not root.left and not root.right):
        return

    flatten(root.left)
    flatten(root.right)

    if not root.left:
        return

    lt=root.left

    while lt and lt.right:
        lt=lt.right

    lt.right=root.right

    root.right=root.left
    root.left=None

    return

