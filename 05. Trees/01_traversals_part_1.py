
from bst import BST

# Problem statement: Implement in-order, pre-order and post-order traversal of a binary search tree using recursion
#
# Algorithm:
# 1. In-order traversal:
#       i. Traverse the left subtree by recursively calling the in-order function.
#       ii. Display the data part of the root (or current node).
#       iii. Traverse the right subtree by recursively calling the in-order function.

# 2. Pre-order traversal:
#       i. Display the data part of the root (or current node).
#       ii. Traverse the left subtree by recursively calling the pre-order function.
#       iii. Traverse the right subtree by recursively calling the pre-order function.

# 3. Post-order traversal:
#       i. Traverse the left subtree by recursively calling the post-order function.
#       ii. Traverse the right subtree by recursively calling the post-order function.
#       iii. Display the data part of the root (or current node).
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def traverse_in_order(node):
    if node is None:
        return

    traverse_in_order(node.left)
    print(node.value, end=" ")
    traverse_in_order(node.right)


def traverse_pre_order(node):
    if node is None:
        return

    print(node.value, end=" ")
    traverse_pre_order(node.left)
    traverse_pre_order(node.right)


def traverse_post_order(node):

    if node is None:
        return

    traverse_post_order(node.left)
    traverse_post_order(node.right)
    print(node.value, end=" ")


def main():

    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(17)

    traverse_in_order(bst.root)
    print()
    traverse_pre_order(bst.root)
    print()
    traverse_post_order(bst.root)
    print()


main() #calling main function

# Output:
# 2 5 7 10 12 15 17 # In-order
# 10 5 2 7 15 12 17 # Pre-order
# 2 7 5 12 17 15 10 # Post-order
