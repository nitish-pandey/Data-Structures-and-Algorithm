

# Problem Statement: Finding the majority element in an array
# Majority element is the element that appears more than n/2 times in an array of size n


# Approach 1: Using Hashing

# Time Complexity: O(n)
# Space Complexity: O(n)

def majority_element_hashing(arr):

    # Creating a dictionary to store the frequency of each element
    frequency = {}

    # Iterating through the array to store the frequency of each element
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    # Iterating through the dictionary to find the element with frequency > n/2
    for key, value in frequency.items():
        if value > len(arr) // 2:
            return key

    # If no element is found, returning -1
    return -1



# Approach 2: Using Moore's Voting Algorithm

# Time Complexity: O(n)
# Space Complexity: O(1)


# Algorithm:
# 1. Initialize a variable 'majority_element' to store the majority element
# 2. Initialize a variable 'count' to store the frequency of the majority element
# 3. Iterate through the array
# 4. If the count is 0, update the majority element to the current element
# 5. If the current element is equal to the majority element, increment the count
# 6. Else, decrement the count
# 7. Return the majority element


def majority_element_moore(arr):

    # Initializing variables
    majority_element=-1
    count=0

    # Iterating through the array
    for element in arr:

        # If count is 0, updating the majority element to the current element
        if count==0:
            majority_element=element

        # If the current element is equal to the majority element, incrementing the count
        if element==majority_element:
            count+=1

        # Else, decrementing the count
        else:
            count-=1


    # check if the majority element is actually the majority element

    # Initializing the count to 0
    count=0

    # Iterating through the array to find the frequency of the majority element
    for element in arr:
        if element==majority_element:
            count+=1

    # If the frequency is greater than n/2, returning the majority element  
    if count>len(arr)//2:

        return majority_element

    # Else, returning -1
    else:
        return -1

