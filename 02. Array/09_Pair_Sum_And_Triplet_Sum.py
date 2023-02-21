
# Problem Statement : You are given a array and the sum s. You have to find if there exists a pair of elements in the array whose sum is equal to s.

# Approach : Using Hashing



# Algorithm:
# 1. Initialize a variable 'hash_table' to store the elements of the array
# 2. Iterate through the array
# 3. If the difference between the sum and the current element is present in the hash table, return True
# 4. Else, add the current element to the hash table
# 5. Return False

# Time Complexity: O(n)
# Space Complexity: O(n)

def pair_sum(arr,s):

    # Initializing the hash table
    hash_table={}

    # Iterating through the array
    for element in arr:

        # If the difference between the sum and the current element is present in the hash table, returning True
        if s-element in hash_table:
            return True

        # Else, adding the current element to the hash table
        else:
            hash_table[element]=1

    # If the difference is not present in the hash table, returning False
    return False



# Problem Statement : You are given a sorted array and the sum s. You have to find if there exists a pair of elements in the array whose sum is equal to s.

# Approach: Using two pointers

# Algorithm:
# 1. Initialize two variables 'left' and 'right' to store the left and right pointers
# 2. Iterate through the array
# 3. If the sum of the elements at the left and right pointers is equal to the sum, return True
# 4. If the sum of the elements at the left and right pointers is less than the sum, increment the left pointer
# 5. Else, decrement the right pointer
# 6. Return False

# Time Complexity: O(n)
# Space Complexity: O(1)

def pair_sum_sorted(arr,s):

    # Initializing the left and right pointers
    left=0
    right=len(arr)-1

    # Iterating through the array
    while left<right:

        # If the sum of the elements at the left and right pointers is equal to the sum, returning True
        if arr[left]+arr[right]==s:
            return True

        # If the sum of the elements at the left and right pointers is less than the sum, incrementing the left pointer
        elif arr[left]+arr[right]<s:
            left+=1

        # Else, decrementing the right pointer
        else:
            right-=1

    # If the sum is not found, returning False
    return False




# Problem Statement : You are given a array and the sum s. You have to find if there exists a triplet of elements in the array whose sum is equal to s.

# Approach: Using sorting

# Algorithm:
# 1. Sort the array
# 2. Iterate through the array
# 3. For each element, find the pair sum of the sum and the current element
# 4. If the pair sum is found, return True
# 5. Else, return False


# Time Complexity: O(n^2)
# Space Complexity: O(1)

def triplet_sum(arr,s):

    # Sorting the array
    arr.sort()

    # Iterating through the array
    for i in range(len(arr)):

        # Finding the pair sum of the sum and the current element
        if pair_sum_sorted(arr[i+1:],s-arr[i]):
            return True

    # If the pair sum is not found, returning False
    return False