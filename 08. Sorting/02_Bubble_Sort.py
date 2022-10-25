
# Problem Statement: Sort the array using Bubble Sort

# Approach: Swap the adjacent elements if they are not in the correct order

# Algorithm:
# 1. Iterate from 0 to n-1
# 2. Iterate from 0 to n-1-i
# 3. If arr[j]>arr[j+1], swap the elements
# 4. Repeat the same process for the remaining elements

# Time Complexity: O(n^2) in all case
# Space Complexity: O(1)


def bubble_sort(arr):

    n=len(arr)

    for i in range(n-1):

        for j in range(1,n-i):

            if arr[j-1]>arr[j]:

                arr[j],arr[j-1]=arr[j-1],arr[j]

    return arr



def main():

    arr=[23,45,12,67,89,34,56,90,1,2,3,4,5,6,7,8,9,10]

    ans=bubble_sort(arr)

    print(ans)


# main() # calling the  main function

# Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 23, 34, 45, 56, 67, 89, 90]

