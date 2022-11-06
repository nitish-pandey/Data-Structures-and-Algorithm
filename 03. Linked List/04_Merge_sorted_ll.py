from linked_list import *

# Problem Statement: Merge two sorted linked lists

# Tags: Two Pointers approach

# Approach: Use Two pointers, one for each list. Compare the data of the nodes pointed by the pointers and insert the smaller one into the new list. Move the pointer of the list whose node was inserted. Repeat until one of the lists is empty. Then, append the remaining list to the new list.



# Algorithm:
# 1. Initialize 3 pointers, curr1, curr2 and curr to head1, head2 and head respectively
# 2. Iterate through the lists until one of them is empty
# 3. Compare the data of the nodes pointed by curr1 and curr2
# 4. Insert the smaller one into the new list
# 5. Move the pointer of the list whose node was inserted
# 6. Repeat until one of the lists is empty
# 7. Append the remaining list to the new list
# 8. Return the new list

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)


def merge_sorted_ll(head1,head2):
    
    curr1=head1
    curr2=head2

    head=node()
    curr=head

    while curr1 and curr2:

        if curr1.data<curr2.data:
            curr.next=curr1
            curr1=curr1.next
        else:
            curr.next=curr2
            curr2=curr2.next
        curr=curr.next

    if curr1:
        curr.next=curr1

    if curr2:
        curr.next=curr2


    ll=linked_list()
    ll.head=head.next

    return ll




def main():
    l1 = linked_list()
    l2 = linked_list()

    l1.insert_last(5)
    l1.insert_last(10)
    l1.insert_last(15)
    l2.insert_last(2)
    l2.insert_last(3)
    l2.insert_last(20)

    l1.print_list()
    l2.print_list()

    l3=merge_sorted_ll(l1.head,l2.head)

    l3.print_list()


main() # Call to main()

# Output:
# 2 3 5 10 15 20
