
from linked_list import *

# Problem Statement: Find if a linked list has a cycle ( and remove it if it does )

# Algorithm:
# 1. Take two pointers p1 and p2
# 2. Move p1 by one node and p2 by two nodes
# 3. If p1 and p2 meet, then there is a cycle
# 4. If p1 or p2 becomes None, then there is no cycle


# To remove the cycle ( if it exists ) we can use the continue with algorithm:

# 5. Move p1 to the head of the linked list
# 6. Move p1 and p2 by one node
# 7. When p1 and p2 meet, the node at which they meet is the start of the cycle
# 8. Move p2 to the last node of the linked list

# Time Complexity:     O(n)
# Space Complexity:    O(1)



def find_and_remove_cycle(root):

    if not root:
        return 0

    p1=root
    p2=root

    while p1 and p2:

        p1=p1.next
        p2=p2.next

        if p2:
            p2=p2.next

        if p1==p2:
            break

    if not p1 or not p2:
        return 0

    # Cycle found
    # Remove the cycle

    p1=root

    while p1.next!=p2.next:
        p1=p1.next
        p2=p2.next

    p2.next=None

    return 1


def main():

    ll=linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    print("Before:")
    ll.print_list()
    ll.head.next.next.next.next.next=ll.head.next.next # adding cycle in linked list

    if find_and_remove_cycle(ll.head):
        print("\nCycle Found and removed")
    else:
        print("Cycle not found")

    
    ll.print_list()



main() # Call to main()

# Output:
# Before:
# 5 4 3 2 1

# Cycle Found and removed
# 5 4 3 2 1
