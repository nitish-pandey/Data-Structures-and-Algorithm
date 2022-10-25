

# Problem Statement : Sort the given array with selection sort

# Approach: Find the minimum element in the array and swap it with the first element. 
#               Repeat the same process for the remaining elements.


# Algorithm:
# 1. Iterate from 0 to n-1
# 2. Find the minimum element in the array
# 3. Swap the minimum element with the first element
# 4. Repeat the same process for the remaining elements


# Time Complexity: O(n^2)
# Space Complexity: O(1)


def selection_sort(arr):

    n=len(arr)

    for i in range(n):

        min_index=i

        for j in range(i+1,n):

            if arr[j]<arr[min_index]:

                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr




# Driver Code

def main():

    arr=[23,45,12,67,89,34,56,90,1,2,3,4,5,6,7,8,9,10]

    ans=selection_sort(arr)

    print(ans)



main()

# Output

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 23, 34, 45, 56, 67, 89, 90]