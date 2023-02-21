
# find duplicates in n time complexity and n space complexity


# Algorithm
# 1. Initialize s=set() and dup=[]
# 2. Iterate through arr
# 3. If i in s then append i to dup
# 4. Else add i to s
# 5. return dup

# Time complexity: O(n)
# Space complexity: O(n)

def find_duplicates(arr):
    n=len(arr)
    if n<=1:
        return []
    s=set()
    dup=[]

    for i in arr:
        if i in s:
            dup.append(i)
        else:
            s.add(i)
    return dup

def main():
    arr=[1,2,4,5,6,7,8,9,3,4,5,6,7,8,9,100]
    ans=find_duplicates(arr)
    print(ans)


main() # call main function

# output
# [4, 5, 6, 7, 8, 9]


# Problem Statement 2: You are given a sorted array, remove the duplicates in-place
# 
# Return the no. of elements in non-duplicate array, the numbers should be placed in first k position of same array

# Approach: 2 Pointers

# Algorithm:
# 1. Initialize a variable ind=1
# 2. Iterate from 1 to n:
# 3. If the ith element is not equal prev element:
# 4.    assign the current element to ind and increment ind



# Time Complexity: O(N)
# Space Complexity: O(1)


def remove_dup(arr:list):

    ind=1

    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[ind]=arr[i]
            ind+=1

    return ind