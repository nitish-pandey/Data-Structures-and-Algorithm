

# Problem Statement: Sort a list of numbers using heap sort



# 1. Create a function heap_sort() that takes an array as an argument
# 2. Set n to the length of the array
# 3. Iterate through the array using a for loop starting from n//2-1 to 0
# 4. Call the heapify function using the array, n and i as the arguments
# 5. Iterate through the array using a for loop starting from n-1 to 0
# 6. Swap the elements at index 0 and i
# 7. Call the heapify function using the array, i and 0 as the arguments
# 8. Return the sorted array


# Time Complexity: O(nlogn)
# Space Complexity: O(1)


def heap_sort(arr):

    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr



# Problem : Heapify an array

# Algorithm:

# 1. set largest to i, left to 2*i+1 and right to 2*i+2
# 2. If left is less than n and the element at index left is greater than the element at index largest, set largest to left
# 3. If right is less than n and the element at index right is greater than the element at index largest, set largest to right
# 4. If largest is not equal to i, swap the elements at index i and largest
# 5. Call the heapify function using the array, n and largest as the arguments


def heapify(arr, n, i):

    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)




def main():

    arr = [12, 11, 13, 5, 6, 7]
    print(heap_sort(arr))



main() # Call the main function

# Output:
# [5, 6, 7, 11, 12, 13]