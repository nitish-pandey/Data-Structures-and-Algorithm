from linked_list import *

# Problem Statement 1: Odd Even Linked List
# You are given a linked list. You have to rearrange the linked list such that all the odd nodes are present before the even nodes.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Tags: Two Pointers approach

# Approach:
# We have to change next of every even node to next of its next odd node.
# We have to change next of every odd node to next of its next even node.


# Algorithm:
# 1. Initialize two pointers odd  with head , even and even-start with head.next
# 2. Iterate while even and even.next is not None
# 3. odd.next = even.next
# 4. odd = odd.next
# 5. even.next = odd.next
# 6. even = even.next
# 7. odd.next = even-start
# 8. Return head


# Time Complexity: O(n)
# Space Complexity: O(1)

def odd_even_rearrange(head):

    if not head or not head.next:
        return head

    odd=head
    even=head.next
    even_start=head.next

    while odd and even and even.next:

        odd.next=even.next
        odd=odd.next

        even.next=odd.next
        even=even.next

    odd.next=even_start

    return head


# <-- End of Program -->


# Problem Statement: Pairwise swap elements of a linked list
# You are given a linked list. You have to swap the elements pairwise.

# Example:
# Input: 1->2->3->4->5->6->NULL
# Output: 2->1->4->3->6->5->NULL


def pairwise_swap(head):

    if not head or not head.next:
        return head
        



def main():

    ll=linked_list()
    ll.insert(6)
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)

    ll.print_list()
    ll.head=odd_even_rearrange(ll.head)
    ll.print_list()



main()

