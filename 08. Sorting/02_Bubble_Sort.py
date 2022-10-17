
# Problem statement: Sort a list of numbers using bubble sort

# Algorithm:

# 1. Iterate through the array using  'for loop' using i as the index
# 2. Iterate through the array again using  'for loop' using j as the index
# 3. If the element at index j is greater than the element at index j+1, swap the elements
# 4. Return the sorted array

# Time Complexity: O(n^2)
# Space Complexity: O(1)


def bubble_sort(arr):

    n=len(arr)

    if n<=1:
        return 

    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]



def main():

    arr=[64,25,12,22,11]
    bubble_sort(arr)
    print(arr)


main() # Call to main() function


# Output:
# [11, 12, 22, 25, 64]
