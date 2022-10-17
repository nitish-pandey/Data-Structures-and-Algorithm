

# Problem Statement: Sort a list of numbers using selection sort

# Algorithm:

# 1. Create a function selection_sort() that takes an array as an argument
# 2. Iterate through the array using a for loop
# 3. Set the min_index to i
# 4. Iterate through the array again using a for loop
# 5. If the element at index j is less than the element at index min_index, set min_index to j
# 6. Swap the elements at index i and min_index
# 7. Return the sorted array



# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



def main():

    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))


main() # Call to main() function

# Output:
# [11, 12, 22, 25, 64]