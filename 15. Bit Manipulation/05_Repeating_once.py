
# Problem Statement: You are given an array of integers. Every element appears twice except for one. Find that single one.

# Approach: Using XOR operation

# Algorithm:
# 1. Initialize a variable 'result' to store the result
# 2. Iterate through the array
# 3. XOR the result with the current element
# 4. Return the result

# Time Complexity: O(n)
# Space Complexity: O(1)


def repeating_once(arr):

    # Initializing the result
    result=0

    # Iterating through the array
    for element in arr:

        # XORing the result with the current element
        result^=element

    # Returning the result
    return result


