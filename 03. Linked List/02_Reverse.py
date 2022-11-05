
from linked_list import *

# Table of Contents:
# 1. Reverse a linked list iteratively
# 2. Reverse a linked list recursively
# 3. Reverse a linked list in groups of given size




# Problem Statement 1 : Reverse a linked list iteratively

# Algorithm:
# 1. Initialize three pointers: prev as NULL, curr as head and next as head.next
# 2. Iterate through the linked list While current is not null. In loop, do following.
#    a. Change the next of current node to point to prev
#    b. Move prev and curr one step forward
#    c. If next is not null, move next one step forward
# 3. Return prev

# Time Complexity:     O(n)
# Space Complexity:    O(1)

def reverse(root):
    
    if not root or not root.next:
        return

    prev=None
    curr=root
    next=root.next

    while curr:
        curr.next=prev
        prev=curr
        curr=next
        if next:
            next=next.next

    return prev




# <-- End of Program -->




# Problem Statement 2: Reverse a linked list using recursion


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



# <-- End of Program -->


# Problem Statement 3: Reverse a linked list in groups of given size

# Approach: We will reverse first k nodes using above method and then recursively call the function for further
# Later combinimg and returning the result

# Algorithm:
# 1. Initialize three pointers: prev as NULL, curr as head and next as head.next
# 2. Iterate through the linked list While current is not null k-times only . In loop, do following.
#    a. Change the next of current node to point to prev
#    b. Move prev and curr one step forward
#    c. If next is not null, move next one step forward
# 3. Recursively call the function for further nodes(curr) and store the result in root.next
# 4. Return prev


def reverse_in_groups(root, k):

    if not root or not root.next:
        return root

    prev=None
    curr=root
    next=root.next
    count=k

    while curr and count:
        curr.next=prev
        prev=curr
        curr=next
        if next:
            next=next.next
        count-=1

    root.next=reverse_in_groups(curr, k)
    
    return prev



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
