
# Subarray is the contiguous part of an array
# For example: [1,2,3] is a subarray of [1,2,3,4,5]
#               [1,2,3,4,5] is a subarray of [1,2,3,4,5]
#               [1,2,3,4,5] is a subarray of [0,1,2,3,4,5]

# Table of Contents:
# 1. Maximum sum of all possible subarrays of array (Kadane's Algorithm)
# 2. Maximum sum of all possible subarry of cyclic array
# 3. Maximum product of all possible subarray 
# 4. Subarray with the given sum

# Tags: Array, Sliding Window Technique 


# Problem Statement 1: Maximum sum of all possible subarrays of array (Kadane's Algorithm)

# Kadane Algorithm is used to find the maximum sum of all the possible subarrays


# Algorithm
# 1. Initialize max_sum=arr[0] and curr_sum=arr[0]
# 2. Iterate over the array from 1 to n-1
# 3. curr_sum=max(arr[i],curr_sum+arr[i])
# 4. max_sum=max(curr_sum,max_sum)
# 5. return max_sum


# Time complexity: O(n)
# Space complexity: O(1)

def max_subarray(arr):
    n=len(arr)
    if n==0:
        return 0
    if n==1:
        return arr[0]

    max_sum=arr[0] # max_sum is the maximum sum of all the possible subarrays
    curr_sum=arr[0] # curr_sum is the sum of the current subarray

    for i in range(1,n): # starting from 1 because we have already taken arr[0] in curr_sum
        curr_sum=max(arr[i],curr_sum+arr[i]) 
        max_sum=max(curr_sum,max_sum)
    return max_sum



# Problem Statement 2: Maximum sum of all possible subarry of cyclic array

# Tags: Array, Sliding Window Technique




# Problem Statement 3: Maximum product of all possible subarray



# Algorithm
# 1. Initialize curr_max=arr[0] and curr_min=arr[0] and max_product=arr[0]
# 2. Iterate from 1 to n-1
# 3. If arr[i]<0 then swap curr_max and curr_min
# 4. curr_max=max(arr[i],curr_max*arr[i])
# 5. curr_min=min(arr[i],curr_min*arr[i])
# 6. max_product=max(curr_max,max_product)
# 7. return max_product


# Time complexity: O(n)
# Space complexity: O(1)



def max_subarray(arr):
    n=len(arr)
    if n==0:
        return 0
    if n==1:
        return arr[0]

    curr_max=arr[0]
    curr_min=arr[0]
    max_product=arr[0]

    for i in range(1,n):

        if arr[i]<0:
            curr_max,curr_min=curr_min,curr_max
        
        curr_max=max(arr[i],curr_max*arr[i])
        curr_min=min(arr[i],curr_min*arr[i])

        max_product=max(curr_max,max_product)

    return max_product





# Problem Statement 4: Subarray with the given sum


# Algorithm:
# 1. Initialize start=0 and end=1 and curr_sum=arr[0]
# 2. Iterate over the array from 1 to n
# 3.    while curr_sum>s and start<end-1:
# 4.        curr_sum-=arr[start]
# 5.        start+=1
# 6.    if curr_sum==s:
# 7.        return arr[start,end]
# 8.    if end<n:
# 9.        curr_sum+=arr[end]
# 10.   end+=1
# 11. return []



def subarray_with_given_sum(arr,s):

    n=len(arr)

    if n==0 or sum(arr)<s:
        return []

    start=0
    end=1
    curr_sum=arr[0]

    while end<=n:

        while curr_sum>s and start<end-1:
            curr_sum-=arr[start]
            start+=1
        
        if curr_sum==s:
            return arr[start,end]

        if end<n:
            curr_sum+=arr[end]

        end+=1

    return []