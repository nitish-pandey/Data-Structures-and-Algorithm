
# Problem Statement: Sort a list of numbers using insertion sort

# Algorithm:

# 1. Iterate through the array in reverse using a for loop
# 2. Set the key to the element at index i and j to i-1
# 3. While j is greater than or equal to 0 and key is less than the element at index j
# 4. Set the element at index j+1 to the element at index j
# 5. Decrement j by 1
# 6. Set the element at index j+1 to key
# 7. Return the sorted array



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