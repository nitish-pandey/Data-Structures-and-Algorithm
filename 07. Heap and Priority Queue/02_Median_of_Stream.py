from pq import minHeap, maxHeap
# Problem Statement: You are given a stream of numbers. Compute the median for each new element .

# Example:
# For example, given the sequence 5, 15, 1, 3, we should return 5, 10, 5, 4.

# Approach:
# We can use a min heap and a max heap to solve this problem. 
# The min heap will store the larger half of the numbers while the max heap will store the smaller half of the numbers. 
# This way we can efficiently find the median by retrieving the top element from the heaps. 

# Algorithm:
# 1. Create a min heap and a max heap.
# 2. For each new number, add it to the min heap.
# 3. Pop the top element from the min heap and add it to the max heap.
# 4. If the size of the min heap is smaller than the max heap, pop the top element from the max heap and add it to the min heap.
# 5. If both heaps are the same size, the median is the average of the top elements of the heaps.
# 6. If the min heap is larger, its top element is the median.


# Time Complexity: O( n log n) 
# Space Complexity: O(n) for storing the heaps.

def insert(max_heap,min_heap,data):

    min_heap.push(data)
    max_heap.push(min_heap.pop())

    if min_heap.size()<max_heap.size():
        min_heap.push(max_heap.pop())


def get_median(max_heap,min_heap):

    if min_heap.size() == max_heap.size():
        return (min_heap.peek()+max_heap.peek())/2
    else:
        return min_heap.peek()
    


def stream_median(stream):

    min_heap = minHeap()
    max_heap = maxHeap()

    ans=[]

    for num in stream:

        insert(max_heap,min_heap,num)
        ans.append(get_median(max_heap,min_heap))

    return ans



def main():

    stream=[5,15,1,3]

    print(stream_median(stream))



main() # call main function


# Output:
# [5, 10.0, 5, 4.0]