
from linked_list import *

# Problem Statement: Find if a linked list has a cycle ( and remove it if it does )

# Algorithm:
# 1. Use two pointers slow and fast
# 2. Move slow pointer by one and fast pointer by two
# 3. If they meet, then there is a cycle
# 4. If they don't meet, then there is no cycle


# Continue with below Procedure to remove cycle from linked list
# 5. set slow to head
# 6. if slow==fast, move fast to next until fast.next!=slow
# 6. else move slow and fast by one while next of slow and fast are not equal
# 7. set next of fast to None
# 8. return 1


# Time Complexity:     O(n)
# Space Complexity:    O(1)



def find_and_remove_cycle(root):

    if not root or not root.next:
        return 0

    slow=root
    fast=root

    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            break

    if slow!=fast:
        return 0

    slow=root

    if slow==fast:
        while fast.next!=slow:
            fast=fast.next

    else:
        while slow.next!=fast.next:
            slow=slow.next
            fast=fast.next

    fast.next=None

    return 1


# <-- End of Program -->


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
