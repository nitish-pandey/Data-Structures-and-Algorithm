
from linked_list import *


# Problem Statement 1: Find the middle element of a linked list

# Approach: Use two pointers, one moves twice as fast as the other. When the fast pointer reaches the end, the slow pointer will be at the middle.

# Tag: Two Pointers approach

# Algorithm:
# 1. Intialize 2 pointers, fast and slow to head
# 2. Iterate through the list until fast reaches the end
# 3. fast moves twice as fast as slow
# 4. When fast reaches the end, slow will be at the middle




# Time Complexity: O(n)
# Space Complexity: O(1)

def find_middle(head):

    if not head:
        return

    fast=head
    slow=head

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next

    print("Middle element is: ",slow.data)
    return


# <-- End of Program -->


# Problem Statement 2: Find the nth element from the end of a linked list

# Approach: Use two pointers, one moves n steps ahead of the other. When the fast pointer reaches the end, the slow pointer will be at the nth element from the end.

# Algorithm:
# 1. Intialize 2 pointers, ahead and behind to head
# 2. Move ahead pointer n steps ahead
# 3. Iterate through the list until ahead reaches the end
# 4. behind will be at the nth element from the end, when ahead reaches the end


def nth_from_end(head,n):

    if not head:
        return

    ahead=head
    behind=head

    for i in range(n):
        ahead=ahead.next

    while ahead:
        ahead=ahead.next
        behind=behind.next

    print("Element at ",n,"from the end is: ",behind.data)
    return


# <-- End of Program -->



def main():

    ll=linked_list()

    ll.insert_last(6)
    ll.insert_last(5)
    ll.insert_last(4)
    ll.insert_last(3)
    ll.insert_last(2)
    ll.insert_last(1)

    ll.print_list()

    print()
    find_middle(ll.head)

    print()
    nth_from_end(ll.head,2)





main()

# Output:

# The Linked list is :
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->  NULL
# 
# Middle element is:  4
# 
# Element at  2 from the end is:  5

