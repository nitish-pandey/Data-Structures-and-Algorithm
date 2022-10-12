
from linked_list import *


# Problem Statement: Find the middle element of a linked list

# Algorithm:
# 1. Initialize two pointers slow and fast.
# 2. Make slow point to the head of the linked list and fast point to the second node.
# 3. While fast is not NULL, do the following:  
#     a. Make slow point to the next node.  
#     b. Make fast point to the next node.
#     c. If fast is not NULL, make fast point to the next node.
# 4. Print the data of the node pointed to by slow.

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_middle(ll):

    if not ll.head:
        return None

    slow=ll.head
    fast=ll.head.next

    while fast:

        slow=slow.next
        fast=fast.next

        if fast:
            fast=fast.next

    print(slow.data)



def main():

    ll=linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.print_list()
    find_middle(ll)



main()

# Output:
# 5 4 3 2 1
# 3
