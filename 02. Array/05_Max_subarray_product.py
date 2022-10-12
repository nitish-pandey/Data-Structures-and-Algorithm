
# finding the maximum product of all the possible subarrays
# Tags: Array, Sliding Window Technique

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


def main():
    arr=[-2,1,-3,4,-1,0,2,1,-5,4]
    print(max_subarray(arr))


main() # call main function

# output
# 24