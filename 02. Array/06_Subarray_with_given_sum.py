
# Problem Statement: Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
# Tags: Array, Sliding Window Technique

# Algorithm:
# 1. Initialize i=0, j=0 and sum=0
# 2. Iterate from j=0 to n-1
# 3. Add arr[j] to sum
# 4. If sum==s then return i+1 and j+1
# 5. If sum>s then subtract arr[i] from sum and increment i
# 6. Increment j
# 7. If no subarray found then return -1

# Time complexity: O(n)
# Space complexity: O(1)


def subarray_sum(arr, s):

    n=len(arr)
    i = 0
    j = 0
    sum = 0

    while j < n:
        sum += arr[j]
        if sum == s:
            return i+1, j+1
        elif sum > s:
            sum -= arr[i]
            i += 1
        j += 1
    
    return -1


def main():
    arr=[1,2,3,7,5]
    s=12
    print(subarray_sum(arr,s))


main() # call main function

# output
# (2, 4)
