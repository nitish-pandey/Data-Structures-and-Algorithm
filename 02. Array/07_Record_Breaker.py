
# Problem Statement: You are given a array of no. of visitors in a park for n consecutive days.
# The i-th day had A[i] visitors. The day is considered as a record breaking day if it satisfies
# both the conditions:
# 1. The number of visitors on the day is strictly larger than the number of visitors on each of the previous days. 
# 2. Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.

# Tags: Sliding Window

# Algorithm:
# 1. Initialize a variable curr_max to -1 and count to 0.
# 2. Iterate over the array and check if the current element is greater than curr_max and the next element.
# 3. If yes, then increment count by 1.
# 4. Update curr_max to the current element.
# 5. Return count.

# Time Complexity: O(n)
# Space Complexity: O(1)

def record_breaking_day(arr:list()):
    n=len(arr)

    curr_max=-1
    count=0

    for i in range(n):

        ans=1
        if curr_max>=arr[i]:
            ans=0

        if i<n-1 and arr[i+1]>=arr[i]:
            ans=0
        
        curr_max=max(curr_max,arr[i])
        count+=ans

    return count
