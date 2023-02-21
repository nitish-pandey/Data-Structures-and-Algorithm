

# Problem Statement: Finding the majority element in an array
# Majority element is the element that appears more than n/2 times in an array of size n


# Approach : Using Moore's Voting Algorithm

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



# Problem statement 2: Finding the majority element in an array and return all the majority elements
# Majority element is the element that appears more than n/3 times in an array of size n

# Approach: Using Moore's Voting Algorithm

# Algorithm:
# 1. Initialize two variables 'maj1' and 'maj2' to store the majority elements
# 2. Initialize two variables 'count1' and 'count2' to store the frequency of the majority elements
# 3. Iterate through the array
# 4. If the current element is equal to maj1, increment count1
# 5. If the current element is equal to maj2, increment count2
# 6. If count1 is 0, update maj1 to the current element and increment count1
# 7. If count2 is 0, update maj2 to the current element and increment count2
# 8. Else, decrement count1 and count2
# 9. Iterate through the array again to find the frequency of the majority elements
# 10. If the frequency of maj1 is greater than n/3, append it to the result array
# 11. If the frequency of maj2 is greater than n/3, append it to the result array
# 12. Return the result array


# Time Complexity: O(n)
# Space Complexity: O(1)



def majority_element_moore_2(arr):

    maj1=-1
    maj2=-1
    count1=0
    count2=0


    for i in arr:

        if i==maj1:
            count1+=1
        
        elif i==maj2:
            count2+=1

        elif count1==0:
            maj1=i
            count1+=1

        elif count2==0:
            maj2=i
            count2+=1

        else:
            count1-=1
            count2-=1

    
    count1=0
    count2=0

    for i in arr:
        if i==maj1:
            count1+=1
        elif i==maj2:
            count2+=1

    res=[]
    if count1>len(arr)//3:
        res.append(maj1)

    if count2>len(arr)//3:
        res.append(maj2)

    return res