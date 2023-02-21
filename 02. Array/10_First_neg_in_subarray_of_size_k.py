

# Problem Statement: Given an array of integers and a number k, where 1 <= k <= length of the array.
#  Find the First Negative Integer for each and every window(contiguous subarray) of size k.

# Tags: Array, Sliding Window

# Input: arr[] = {-8, 2, 3, -6, 10}, k = 2
# Output: -8 0 -6 -6

# Input: arr[] = {12, -1, -7, 8, -15, 30, 16, 28}, k = 3
# Output: -1 -1 -7 -15 -15 0

# Algorithm
# 1. Create a variable ind to store the index of the first negative number in the current window and initialize it to 0.
# 2. Traverse the array from 0 to k-1 and find the index of the first negative number in the current window.
# 3. If there is no negative number in the current window, then append 0 to the answer array.
# 4. If there is a negative number in the current window, then append the negative number to the answer array.
# 5. Traverse the array from k to n-1 and do the following steps:   
#     a. If the index of the first negative number in the current window is less than or equal to i-k, then increment the index by 1.
#     b. If the index of the first negative number in the current window is greater than i-k, then increment the index by 1 until the index is less than i and the number at the index is positive.
#     c. If the index of the first negative number in the current window is less than i and the number at the index is negative, then append the number to the answer array.
#     d. If the index of the first negative number in the current window is less than i and the number at the index is positive, then append 0 to the answer array.


# Time Complexity: O(n)
# Space Complexity: O(n)




def first_negs_in_subarray(arr:list, k:int,n:int)->list:

    ans=[]
    ind=0

    for i in range(k):
        if arr[i]<0:
            ind=i
            break
    ans.append(arr[ind] if arr[ind]<0 else 0)


    for i in range(k,n):

        if ind<=i-k:
            ind+=1

        while ind<i and arr[ind]>=0:
            ind+=1
            if arr[ind]<0:
                break

        ans.append(arr[ind] if arr[ind]<0 else 0)

    return ans




def main():

    arr=[-8, 2, 3, -6, 10]
    k=2
    n=len(arr)
    print(first_negs_in_subarray(arr,k,n))

    arr=[12, -1, -7, 8, -15, 30, 16, 28]
    k=3
    n=len(arr)
    print(first_negs_in_subarray(arr,k,n))




main() # call main function

# Output
# [-8, 0, -6, -6]
# [-1, -1, -7, -15, -15, 0]