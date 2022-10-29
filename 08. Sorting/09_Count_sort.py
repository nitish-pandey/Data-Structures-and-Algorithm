
# Problem Statement: Sort the given array using count sort

# Approach:
# Count the frequency of all elements, and calculate cumulative frequency 
# Insert the element in correct position according to cumulative frequency


# Algorithm:
# 1. Find the maximum of array , and create an count array of size m+1
# 2. Count the frequency of all element and save it in count array
# 3. Calculate the cumulative frequency of the count array
# 4. Create a new array for ans, and iterate over original array
# 5. Decrease the value of its cumulative frequency and add this element in the decreased position value
# 6. Return the ans array

# Time Complexity: O(max(arr)+n)
# Space Complexity: O(max(arr)+n)

def count_sort(arr:list()):

    n=len(arr)
    m=max(arr)

    if n<=1:
        return arr

    count_arr=[0]*(m+1)

    for i in arr:
        count_arr[i]+=1

    for i in range(1,m+1):
        count_arr[i]+=count_arr[i-1]

    ans=[0]*n

    for i in range(n-1,-1,-1):

        count_arr[arr[i]]-=1
        ans[count_arr[arr[i]]]=arr[i]

    return ans



def main():

    arr=[1,5,4,2,7,3,9,10,1,3]
    ans=count_sort(arr)

    print(ans)


main()



# Note:
# 1. Count sort is a stable sort
# 2. Count sort is not a comparison sort
# 3. Count sort is not a adaptive sort
# 4. Count sort is used when the range of elements is small
