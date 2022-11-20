
# Problem Statement: You are given a array of size n. Find the K-th largest element. (k<=n)


# Algorithm:
# 1. Convert the array into heap using heapify function
# 2. Pop the first element k times
# 3. Return the popped element

# Note: For the algorithm of Heapify and Build heap refer to the 08. Sorting/heap_sort.py

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

def heapify(heap:list,ind:int,n:int) :

    if ind>=n:
        return

    left = 2*ind+1
    right = 2*ind+2

    largest = ind

    if left<n and heap[left]>heap[largest]:
        largest = left

    if right<n and heap[right]>heap[largest]:
        largest = right

    if largest!=ind:
        heap[ind],heap[largest] = heap[largest],heap[ind]
        heapify(heap,largest,n)



def build_heap(heap:list,n:int) :

    for i in range(n//2,-1,-1):
        heapify(heap,i,n)



def kth_largest(heap:list,k:int) :

    build_heap(heap,len(heap))
    for i in range(len(heap)-1,-1,-1):

        heap[0],heap[i] = heap[i],heap[0]
        heapify(heap,0,i)

    return heap[-k]


# <--End of Code-->



def main():

    arr=[1,2,3,4,5,6,7,8,9,10]

    print(kth_largest(arr,3))



main() # calling to main function

# Output: 8