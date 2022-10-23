
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
