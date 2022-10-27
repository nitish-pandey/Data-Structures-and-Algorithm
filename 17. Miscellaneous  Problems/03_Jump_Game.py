
# Problem Statement: Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Tags: Array, Greedy, Dynamic Programming


# Approach 1: Greedy

# Algorithm:
# 1. Check if size is more than 1, if not return True
# 2. Initialize a variable max_position to save the maximum position upto which it can go
# 4. Iterate over arr from index i  0 to n-1
# 5. If curr position (i.e. i ) is greater than max_position return False
# 6. replace max_position with maximum of curr position + arr[i]  and max_position 
# 7. Return True at the last


# Time Complexity: O(n)
# Space Complexity: O(1)


def can_reach_end_greedy(arr:list()) -> bool:
    n=len(arr)
    if(n<=1):
        return True

    max_position=0

    for i in range(n):
        if i>max_position:
            return False

        max_position=max(max_position,arr[i]+i)

    return True


# Approach 2: Dynamic Programming

# Algorithm:
# 1. Check if size is more than 1, if not return True
# 2. Create a array for dp of size n initializing with False except first one
# 3. Iterate over array form i=0 to n-1
# 4. 