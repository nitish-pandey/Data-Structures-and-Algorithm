
from bst import BST


# Problem statement 1: Implement the left view of a binary tree

# Algorithm:
# 1. Create an empty queue
# 2. Enqueue root node
# 3. While queue is not empty
#       a. Dequeue a node from queue and print it if it is the first node of the current level
#       b. Enqueue left child of the dequeued node
#       c. Enqueue right child of the dequeued node


# Time Complexity: O(n)
# Space Complexity: O(n)


def left_view(root):

    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:

        count = len(queue)

        for i in range(count):

            current = queue.pop(0)

            if i == 0: # for right view, change this to i == count - 1
                print(current.value, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    print()



# Problem statement 2: Implement the top view of a binary tree

# Algorithm:
# 1. Create an empty queue
# 2. Enqueue root node
# 3. create a map/dict to store the horizontal distance of the viewed nodes
# 4. While queue is not empty
#       a. Dequeue a node from queue and add it if the (horizontal distance of the node) is not in the map/dict
#       b. Enqueue left child of the dequeued node
#       c. Enqueue right child of the dequeued node



def top_view(root):

    if root is None:
        return

    queue=[]
    queue.append(root)

    viewed=dict()

    while queue:

        count=len(queue)

        for i in range(count):

            curr=queue.pop(0)
            hd=curr.hd

            if hd not in viewed: # for bottom view, remove this if condition
                viewed[hd]=curr.value

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

    for i in viewed:
        print(viewed[i],end=" ")

    print()





def main():

    bst=BST()
    bst.insert(45)
    bst.insert(89)
    bst.insert(22)
    bst.insert(34)
    bst.insert(12)

    left_view(bst.root)
    top_view(bst.root)


main()


