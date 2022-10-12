
from bst import BST

# Problem Statement: Implement Level Order Traversal of a binary search tree without recursion

# Algorithm:
# 1. Create an empty queue
# 2. Enqueue root node
# 3. While queue is not empty
#       a. Dequeue a node from queue and print it
#       b. Enqueue left child of the dequeued node
#       c. Enqueue right child of the dequeued node

# Time Complexity: O(n)
# Space Complexity: O(n)

def traverse_level_order(node):

    if node is None:
        return

    queue = []
    queue.append(node)

    while queue:

        current = queue.pop(0)
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print()


def main():

    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)

    traverse_level_order(bst.root)


main() # call main function

# Output:
# 10 5 15 2 7 12
