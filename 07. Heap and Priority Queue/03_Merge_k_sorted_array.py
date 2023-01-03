
# Problem Statement: You are given a k-list of sorted array. Merge them into one sorted array.

# Approach: Using Heaps

# Algorithm:
# 1. Create a min heap and add the first element of each array to the heap.
# 2. Pop the top element from the heap and add it to the result array.
# 3. Add the next element from the array from which the element was popped to the heap.
# 4. Repeat steps 2 and 3 until the heap is empty.

# Time Complexity: O( n log k)
# Space Complexity: O(k) for storing the heap.

from pq import minHeap


def merge_k_sorted_array(arrays):

    result = []
    min_heap = minHeap()

    for i in range(len(arrays)):
        min_heap.push((arrays[i][0], i, 0))

    while min_heap.size() > 0:

        num, i, j = min_heap.pop()
        result.append(num)

        if j + 1 < len(arrays[i]):
            min_heap.push((arrays[i][j + 1], i, j + 1))

    return result


def main():

    arrays = [[1, 3, 5, 7], [2, 4, 6], [0, 8, 9, 10, 11]]

    print(merge_k_sorted_array(arrays))



main() # call main function

# Output: 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]