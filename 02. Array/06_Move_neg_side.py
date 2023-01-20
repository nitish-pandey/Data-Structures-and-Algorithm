
# Problem Statement: You are given an array containing few negative elements.
# Move all the negatives to the end of the array keeping the relative position same.


# Algorithm:
# 1. Create a variable ind=-1
# 2. Iterate through the array
# 3. If the element is negative, increment ind by 1 and swap the element with the element at ind
# 4. Return the array


# Time Complexity: O(n)
# Space Complexity: O(1)

def move_neg(arr):

    ind=-1

    for i in range(len(arr)):
        if arr[i]<0:
            ind+=1
            arr[i],arr[ind]=arr[ind],arr[i]


    return arr





