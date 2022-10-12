from linked_list import *

# Problem Statement: 


def merge(l1,l2):

    ptr1=l1.head
    ptr2=l2.head

    l3=linked_list()

    while ptr1 and ptr2:

        if ptr1.data<ptr2.data:
            l3.insert_last(ptr1.data)
            ptr1=ptr1.next
        else:
            l3.insert_last(ptr2.data)
            ptr2=ptr2.next

    while ptr1:
        l3.insert_last(ptr1.data)
        ptr1=ptr1.next

    while ptr2:
        l3.insert_last(ptr2.data)
        ptr2=ptr2.next

    return l3


def main():

    l1=linked_list()
    l1.insert_last(1)
    l1.insert_last(3)
    l1.insert_last(5)
    l1.insert_last(7)

    l2=linked_list()
    l2.insert_last(2)
    l2.insert_last(4)
    l2.insert_last(6)
    l2.insert_last(8)
    
    l3=merge(l1,l2)

    l3.print_list()



main() # call main function

# output
# 1 2 3 4 5 6 7 8 
