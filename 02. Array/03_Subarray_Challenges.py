
# Subarray is the contiguous part of an array
# For example: [1,2,3] is a subarray of [1,2,3,4,5]
#               [1,2,3,4,5] is a subarray of [1,2,3,4,5]
#               [1,2,3,4,5] is a subarray of [0,1,2,3,4,5]

# Table of Contents:
# 1. Maximum sum of all possible subarrays of array (Kadane's Algorithm)
# 2. Maximum sum of all possible subarry of cyclic array
# 3. Maximum product of all possible subarray 
# 4. Subarray with the given sum
# 5. Longest Arithmetic Subarray

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

# Algorithm:
# 1. Find out the maximum subarray sum and minimum subarray sum using Kadane
# 2. Find out the total sum of array
# 3. If minimum subarray sum is equal to total sum of array, return max subarray sum
# 4. Return maximum of maximum subarray sum and (total sum - minimum subarray sum)

# Time complexity: O(n)
# Space complexity: O(1)


def maximum_subarray_sum_cyclic(arr:list()) ->int:
    n=len(arr)

    if n==0:
        return 0


    curr_max,curr_min,max_sum,min_sum=arr[0],arr[0],arr[0],arr[0]
    total_sum=arr[0]

    for i in range(1,n):
        total_sum+=arr[i]

        curr_max=max(arr[i],curr_max+arr[i])
        max_sum=max(max_sum,curr_max)

        curr_min=min(arr[i],curr_min+arr[i])
        min_sum=min(min_sum,curr_min)

    if min_sum==total_sum:
        return max_sum

    return max(max_sum,total_sum-min_sum)

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



# Problem Statement 5: You are given in an array of integers. Find the length of longest arithmetic subarray in the array
# An arithmetic subarray is a subarray in which the difference between consecutive elements is the same

# Tags: Array, Sliding Window Technique


def longest_arithmetic_subarray(arr:list()) ->int:
    n=len(arr)

    if n<3:
        return n

    curr_ans=2
    final_ans=2

    for i in range(2,n):

        d1=arr[i-1]-arr[i-2]
        d2=arr[i]-arr[i-2]

        if d1==d2:
            curr_ans+=1

        else:
            curr_ans=2

        final_ans=max(final_ans,curr_ans)

    
    return final_ans