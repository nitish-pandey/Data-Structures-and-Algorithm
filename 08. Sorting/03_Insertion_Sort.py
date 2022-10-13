
# Problem Statement: Sort a list of numbers using insertion sort

# Algorithm:

# 1. Insert the second element in the list in the sorted list
# 2. Insert the third element in the list in the sorted list
# 3. Repeat steps 1 and 2 for the remaining elements


# Time Complexity: O(n^2)
# Space Complexity: O(1)


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr