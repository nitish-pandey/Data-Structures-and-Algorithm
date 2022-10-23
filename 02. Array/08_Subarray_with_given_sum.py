
# Problem Statement: Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
# Tags: Array, Sliding Window Technique

# Algorithm:
# 1. Initialize start to 0, end to 1 and curr_sum to arr[0]
# 2. Iterate while end is less than or equal to n
# 3. If curr_sum is greater than s and start is less than end-1, then subtract arr[start] from curr_sum and increment start
# 4. If curr_sum is equal to s, return [start, end-1]
# 5. If end is less than n, add arr[end] to curr_sum
# 6. Return [-1]


# Time complexity: O(n)
# Space complexity: O(1)


def subarray_sum(arr, s):
    n=len(arr)

    if n==0:
        return -1

    st=0
    curr_sum=arr[0]

    end=1

    while end<=n:

        while curr_sum>s and st<end-1:
            curr_sum-=arr[st]
            st+=1

        if curr_sum==s:
            return [st,end-1]

        
        if end<n:
            curr_sum+=arr[end]

    return [-1]

def main():
    arr=[1,2,3,7,5]
    s=12
    print(subarray_sum(arr,s))


main() # call main function

# output
# (2, 4)
