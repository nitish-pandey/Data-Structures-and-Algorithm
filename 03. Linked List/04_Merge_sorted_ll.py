from linked_list import *

# Problem Statement: Merge two sorted linked lists
# Tags: Two Pointers approach


# Algorithm:
# 1. Create a new linked list l3
# 2. Traverse both the linked lists l1 and l2
# 3. Compare the data of the nodes of l1 and l2
# 4. Insert the smaller data into l3
# 5. Repeat step 3 and 4 until one of the linked list is exhausted
# 6. Insert the remaining nodes of the other linked list into l3

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)


def merge_sorted_ll(l1, l2):

    l3 = linked_list()
    curr1 = l1.head
    curr2 = l2.head


    while curr1 and curr2:
        if curr1.data < curr2.data:
            l3.insert_last(curr1.data)
            curr1 = curr1.next
        else:
            l3.insert_last(curr2.data)
            curr2 = curr2.next

    while curr1:
        l3.insert_last(curr1.data)
        curr1 = curr1.next

    while curr2:
        l3.insert_last(curr2.data)
        curr2 = curr2.next

    return l3



def main():
    l1 = linked_list()
    l2 = linked_list()

    l1.insert_last(5)
    l1.insert_last(10)
    l1.insert_last(15)
    l2.insert_last(2)
    l2.insert_last(3)
    l2.insert_last(20)

    l3 = merge_sorted_ll(l1, l2)
    l3.print_list()


main() # Call to main()

# Output:
# 2 3 5 10 15 20
