
from stack_and_queue import *


# Problem Statement: Reverse a stack without Recursion and extra space

# Algorithm:
# 1. Initialize three pointers p1, p2 and p3.
# 2. Let p1 point to the first node, p2 point to the second node and p3 point to the third node.
# 3. Make p1 point to NULL.
# 4. While p2 is not NULL, do the following:
#     a. Make p2 point to p1.
#     b. Make p1 point to p2.
#     c. Make p2 point to p3.
#     d. If p3 is not NULL, make p3 point to the next node.
# 5. Make the head of the linked list point to p1.


# Time Complexity: O(n)
# Space Complexity: O(1)



def reverse_stack(st):

    root=st.head

    if not root or not root.next:
        return

    p1=root
    p2=root.next
    p3=p2.next

    p1.next=None

    while p2:

        p2.next=p1
        p1=p2
        p2=p3

        if p3:
            p3=p3.next

    st.head=p1




def main():

    st=stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.print_stack()
    reverse_stack(st)
    st.print_stack()


main()

# Output:
# 5 4 3 2 1
# 1 2 3 4 5

