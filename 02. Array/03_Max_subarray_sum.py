
# finding the maximun sum of all the possible subarrays
# Subarray is a contiguous part of an array

# Tags: Array, Sliding Window Technique

# Kadane Algorithm is used to find the maximum sum of all the possible subarrays

# Time complexity: O(n)
# Space complexity: O(1)

# Algorithm
# 1. Initialize max_sum=arr[0] and curr_sum=arr[0]
# 2. Iterate from 1 to n-1
# 3. curr_sum=max(arr[i],curr_sum+arr[i])
# 4. max_sum=max(curr_sum,max_sum)
# 5. return max_sum

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


def main():
    arr=[-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray(arr))


main() # call main function

# output
# 6