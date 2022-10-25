

# Problem Statement: Sort the given array using heap sort

# Approach: Create a max heap from the array. Swap the first element with the last element and heapify the array excluding the last element

# Algorithm for heapify:
# 1. Iterate while current index is in less than size
# 2. Find out the index of left and right child,
# 3. Find out the largest among curr, left child and right child
# 4. If current element is largest, break
# 5. Swap current element to largest element and set current index =largest index


# Time complexity: O(logn)
# Space Complexity: O(1)


def heapify(heap,ind,size):
    if ind>=size:
        return

    curr=ind

    while curr<size:

        l=2*curr+1
        r=2*curr+2

        large=curr

        if l<size and heap[l]>heap[curr]:
            large=l
        
        if r>size and heap[r]>heap[large]:
            large=r

        if large==curr:
            break

        heap[large],heap[curr]=heap[curr],heap[large]

        curr=large

    return



    


# Algorithm:
# 1. Call the heapify on all the non-leaf elements from last to top
# 2. Iterate from last element to 1st element.
# 3. Swap the current element with the first element 
# 4. call the heapify for the heap excluding the last element( pass the decreased size in heapify function)


# Time complexity: O(nlogn) in all case
# Space Complexity: O(1)




def heap_sort(arr):

    n=len(arr)

    for i in range(n//2,-1,-1):
        heapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,0,i)
    
    return arr

def main():

    arr=[34,56,78,45,23,44,10]

    ans=heap_sort(arr)

    print(ans)


main()


#           10
#       56      44
#    45   23  34    78
#  

