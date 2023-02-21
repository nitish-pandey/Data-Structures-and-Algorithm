
# Problem Statement: Given an array of integers representing an elevation map where the width of each bar is 1, return how much rainwater can be trapped.

# For example, given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Algorithm:
# 1. Initialize the left and right arrays
# 2. Fill the left array with the maximum element to the left of the current element
# 3. Fill the right array with the maximum element to the right of the current element
# 4. Initialize the water variable
# 5. Iterate through the array
# 6. Update the water variable as the minimum of the left and right array at the current index minus the current element
# 7. Return the water variable


# Time Complexity: O(n)
# Space Complexity: O(n)


def trapping_rainwater(arr:list):

    n=len(arr)

    # Initializing the left and right arrays
    left=[0]*n
    right=[0]*n

    # Initializing the left_max and right_max variables
    left_max=0
    right_max=0

    # Iterating through the array
    for i in range(n):

        # Updating the left_max variable
        left_max=max(left_max,arr[i])

        # Updating the left array
        left[i]=left_max


    # Iterating through the array in reverse
    for i in range(n-1,-1,-1):

        # Updating the right_max variable
        right_max=max(right_max,arr[i])

        # Updating the right array
        right[i]=right_max


    # Initializing the water variable
    water=0

    # Iterating through the array
    for i in range(n):

        # Updating the water variable
        water+=min(left[i],right[i])-arr[i]


    # Returning the water variable
    return water