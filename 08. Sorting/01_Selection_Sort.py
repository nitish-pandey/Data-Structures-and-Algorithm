

# Problem Statement: Sort a list of numbers using selection sort

# Algorithm:

# 1. Find the minimum element in the list
# 2. Swap the minimum element with the first element
# 3. Repeat steps 1 and 2 for the remaining list


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