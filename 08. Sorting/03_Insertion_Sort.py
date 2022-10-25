

# problem statement: Sort the given array using insertion Sort

# Approach: Select the element from the unsorted array and place it in correct position in the sorted array

# Algorithm: 
# 1. Iterate from arr[1] to arr[n] over the array
# 2. Compare the current element (key) to its predecessor
# 3. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element

# Time Complexity: O(n^2) in worst case and O(n) in best case
# Space Complexity: O(1)


# Insertion is more efficient for smaller data sets or mostly sorted data sets


def insertion_sort(arr):

    n=len(arr)

    for i in range(1,n):

        j=i-1
        while j>=0 and arr[j]>arr[j+1]:

            arr[j],arr[j+1]=arr[j+1],arr[j]
            j-=1

    return arr



def main():

    arr=[5,4,3,2,1]
    print(insertion_sort(arr))



# main() # calling main function

# Output: [1, 2, 3, 4, 5]