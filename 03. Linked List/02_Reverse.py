
from linked_list import *

# Problem Statement: Reverse a linked list

# Algorithm:
# 1. Take three pointers p1, p2 and p3
# 2. Move p1 to the first node, p2 to the second node and p3 to the third node
# 3. Make p1 point to None
# 4. Make p2 point to p1
# 5. Move p1 to p2, p2 to p3 and p3 to p3.next
# 6. Repeat steps 4 and 5 until p2 is None



# Time Complexity:     O(n)
# Space Complexity:    O(1)

def reverse(root):
    
    if not root or not root.next:
        return

    p1=root
    p2=root.next
    p3=root.next.next

    p1.next=None

    while p2:

        p2.next=p1
        p1=p2
        p2=p3

        if p3:
            p3=p3.next

    return p1

# Output:
# 89 78 67 56 45 34 23
# 23 34 45 56 67 78 89

# Problem Statement: Reverse a linked list using recursion


# Algorithm:
# 1. Return root if root is null or only one node is present
# 2. Call the function recursively on root.next and save it in temp
# 3. Make root.next.next point to root
# 4. Make root.next point to None
# 5. Return temp

# Time Complexity:     O(n)
# Space Complexity:    O(n)

def reverse_recursion(root):

    if not root or not root.next:
        return root

    temp=reverse_recursion(root.next)

    root.next.next=root
    root.next=None

    return temp

def main():

    ll=linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_list()
    ll.head=reverse_recursion(ll.head)
    ll.print_list()



main() # Call to main()


# Output:
# 5 4 3 2 1
# 1 2 3 4 5
