
# Problem Statement: You are given a ladder of n-steps. You can climb either 1 or 2 steps at a time. 
#                       Return the number of possible ways you can climb the ladder.


# Algorithm:
# 1. Create a array of size n+1 to store ans.
# 2. Initialize 0-th and 1-st index as 1
# 3. Iterate i from 2 to n:
#   set arr[i]=arr[i-1]+arr[i-2]
# 4. Return arr[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

def no_of_comb(n:int)->int:

    if n<0:
        return 0

    arr=[1]*(n+1)

    for i in range(2,n+1):
        arr[i]=arr[i-1]+arr[i-2]

    return arr[n]


    