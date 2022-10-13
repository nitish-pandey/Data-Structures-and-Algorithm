
# Problem statement: Sort a list of numbers using bubble sort

# Algorithm:

# 1. Compare the first element with the second element
# 2. If the first element is greater than the second element, swap them
# 3. Compare the second element with the third element
# 4. If the second element is greater than the third element, swap them
# 5. Repeat steps 3 and 4 for the remaining elements
# 6. Repeat steps 1-5 for the remaining elements


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
