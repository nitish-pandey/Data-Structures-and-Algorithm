
from bst import BST

# Problem statement: Implement in-order, pre-order and post-order traversal of a binary search tree without recursion

# Algorithm:

# 1. In-order traversal:
#       i. Create an empty stack.
#       ii. Initialize current node as root.
#       iii. Push the current node to S and set current = current->left until current is NULL.
#       iv. If current is NULL and stack is not empty then
#               a. Pop the top item from stack.
#               b. Print the popped item, set current = popped_item->right
#               c. Go to step 3.
#       v. If current is NULL and stack is empty then we are done.

# 2. Pre-order traversal:
#       i. Create an empty stack and push root to it.
#       ii. Do following while stack is not empty.
#               a. Pop an item from stack and print it.
#               b. Push right child of popped item to stack
#               c. Push left child of popped item to stack

# 3. Post-order traversal:
#       i. Create an empty stack.
#       ii. Initialize current node as root.
#       iii. Push the current node to S and set current = current->left until current is NULL.
#       iv. If current is NULL and stack is not empty then
#               a. Peek the top item from stack.
#               b. If the right child of the top stack item is not processed yet, then set current = popped_item->right
#               c. Else, print the top stack item, pop the stack and set current = NULL
#       v. If current is NULL and stack is empty then we are done.


# Time Complexity: O(n)
# Space Complexity: O(n)


def traverse_in_order(node):

    stack = []
    current = node

    while True:

        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right
        else:
            break


def traverse_pre_order(node):

    stack = []
    stack.append(node)

    while stack:

        current = stack.pop()
        print(current.value, end=" ")

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)



def traverse_post_order(node):

    stack = []
    current = node

    while True:

        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            peek = stack[-1]
            if peek.right is not None:
                current = peek.right
            else:
                print(peek.value, end=" ")
                stack.pop()
                while stack and stack[-1].right == peek:
                    peek = stack.pop()
                    print(peek.value, end=" ")
        else:
            break



def main():

    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)

    print("In-order traversal: ", end="")
    traverse_in_order(bst.root)
    print()

    print("Pre-order traversal: ", end="")
    traverse_pre_order(bst.root)
    print()

    print("Post-order traversal: ", end="")
    traverse_post_order(bst.root)
    print()



main() # call main function


# Output:
# In-order traversal: 2 5 7 10 12 15
# Pre-order traversal: 10 5 2 7 15 12
# Post-order traversal: 2 7 5 12 15 10
