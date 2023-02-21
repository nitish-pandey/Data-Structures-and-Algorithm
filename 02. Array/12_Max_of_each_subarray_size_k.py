from collections import deque

# Problem: Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

# Tags: Array, Sliding Window, Deque

# Algorithm: Sliding Window
# 1. Create a Deque, for keeping track of the maximum element in the current window
# 2. Traverse the array from 0 to k-1 and keep popping the elements from the right of the deque which are smaller than the current element
# 3. Append the current element to the right of the deque
# 4. Append the first element of the deque to the result list
# 5. Traverse the array from k to n-1
# 6. If the first element of the deque is the element going out of the window, then pop it from the left
# 7. Keep popping the elements from the right of the deque which are smaller than the current element
# 8. Append the current element to the right of the deque
# 9. Append the first element of the deque to the result list
# 10. Return the result list

# Time Complexity: O(n)
# Space Complexity: O(k)


def max_of_each_subarray(arr:list,k:int)->list:

    dq=deque()

    res=[]


    for i in range(k):
        while dq and dq[-1]<arr[i]:
            dq.pop()

        dq.append(arr[i])

    
    res.append(dq[0])

    for i in range(k,len(arr)):

        if dq[0]==arr[i-k]:
            dq.popleft()

        while dq and dq[-1]<arr[i]:
            dq.pop()
        dq.append(arr[i])

        res.append(dq[0])

    return res





def main():

    arr=[1,2,3,1,4,5,2,3,6]
    k=3

    print(max_of_each_subarray(arr,k))




main() # call to main function

# Output: [3, 3, 4, 5, 5, 5, 6]