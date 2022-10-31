
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
# 6. Longest Subarray with 0 sum
# 7. Longest Subarray with sum divisible by k
# 8. Longest Subarray with equal number of 0s and 1s

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



# End:


# Problem Statement 2: Maximum sum of all possible subarry of cyclic array

# Tags: Array, Sliding Window Technique

# Algorithm:
# 1. Find out the maximum subarray sum and minimum subarray sum using Kadane
# 2. Find out the total sum of array
# 3. If minimum subarray sum is equal to total sum of array, return max subarray sum
# 4. Return maximum of (maximum subarray sum) and (total sum - minimum subarray sum)

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


# End:


# Problem Statement 3: Maximum product of all possible subarray


# Algorithm
# 1. Initialize curr_max,curr_min,max_product to first element of array
# 2. Iterate over the array from 1 to n-1
# 3. If arr[i] is negative, swap curr_max and curr_min
# 4. Replace curr_max with maximum of arr[i] and curr_max*arr[i]
# 5. Replace curr_min with minimum of arr[i] and curr_min*arr[i]
# 6. Replace max_product with maximum of curr_max and max_product
# 7. Return max_product


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



# End:


# Problem Statement 4: Subarray with the given sum


# Algorithm:
# 1. Initialize start=0 , end=1 and curr_sum=arr[0]
# 2. Iterate over the array from 1 to n
# 3. While curr_sum>s and start<end-1, do curr_sum-=arr[start] and start+=1
# 4. If curr_sum==s, return arr[start,end]
# 5. If curr_sum<s, do curr_sum+=arr[end] and end+=1
# 6. return -1 if no subarray is found

# Time complexity: O(n)
# Space complexity: O(1)

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


# End:


# Problem Statement 5: You are given in an array of integers. Find the length of longest arithmetic subarray in the array
# An arithmetic subarray is a subarray in which the difference between consecutive elements is the same

# Approach: Considering the first two elements are already in Arithmetic Sequence, we will check for the next element
# If the next element is in Arithmetic Sequence, we will increase the length of the subarray
# If the next element is not in Arithmetic Sequence, we will reset the length of the subarray to 2


# Algorithm:
# 1. Initialize current length=2 and max_length=2
# 2. Iterate over the array from 2 to n-1
# 3. If arr[i]-arr[i-1]==arr[i-1]-arr[i-2], increase current length by 1
# 4. Else, reset current length to 2
# 5. Replace max_length with maximum of current length and max_length
# 6. Return max_length at the end

# Time complexity: O(n)
# Space complexity: O(1)


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


# End:


# Problem Statement 6: You are given an array of integers. Find the length of longest subarray in the array such that the sum of elements of subarray is 0

# Approach 1: Hashing
# In this approach we will store the sum of elements of subarray in a hash table and check if the sum is already present in the hash table or not
# If the sum is already present in the hash table, then we will update the length of longest subarray
# If the sum is not present in the hash table, then we will insert the sum in the hash table


# Algorithm:
# 1. Initialize current length=0 , max_length=0 ,curr sum =0  and create a hash table
# 2. Iterate over the array from 0 to n-1
# 3. If sum is already present in the hash table, update current length to i-hash[sum]
# 4. Else, insert sum in the hash table
# 5. Replace max_length with maximum of current length and max_length
# 6. Return max_length at the end

# Time complexity: O(n)
# Space complexity: O(n)


def longest_subarray_with_sum_0(arr:list) ->int:
    n=len(arr)

    if n==0:
        return 0

    curr_length=0
    max_length=0
    curr_sum=0
    hash_table={}

    for i in range(n):
        curr_sum+=arr[i]

        if curr_sum==0:
            curr_length=i+1

        elif curr_sum in hash_table:
            curr_length=i-hash_table[curr_sum]

        else:
            hash_table[curr_sum]=i

        max_length=max(max_length,curr_length)

    return max_length




# Problem Statement 7: You are given an array of integers. Find the length of longest subarray in the array such that the sum of elements of subarray is divisible by k


def longest_subarray_with_sum_divisible_by_k(arr:list,k:int) ->int:
    n=len(arr)
    if n==0:
        return 0

    curr_sum=0
    max_len=0
    h={}

    for i in range(n):

        curr_sum+=arr[i]

        if curr_sum%k==0:
            max_len=i+1

        if curr_sum%k in h:
            max_len=max(max_len,i-h[curr_sum%k])

        else:
            h[curr_sum%k]=i


    return max_len



# Problem Statement 8: You are given an array of integers. Find the length of longest subarray in the array such that the number of 0's and 1's are equal


# Tags: Array, Sliding Window Technique

# Approach: Replace 0 with -1 and then find the longest subarray with sum 0

def longest_subarray_with_equal_0_1(arr:list) ->int:
    n=len(arr)

    if n==0:
        return 0

    for i in range(n):
        if arr[i]==0:
            arr[i]=-1

    return longest_subarray_with_sum_0(arr)


