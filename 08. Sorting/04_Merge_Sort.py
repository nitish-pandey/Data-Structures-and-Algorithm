
# Problem Statement: Given an array of integers nums, sort the array in ascending order using Merge Sort Algorithm.

# Approach: We will use Divide and Conquer Algorithm to solve this problem.
#           We will divide the array into two halves and sort them individually.
#           Then we will merge the two sorted halves into one sorted array.


# Time Complexity: O(nlogn)
# Space Complexity: O(n)


# Algorithm:
# 1. Check if left index is greater than or equal right index. If yes, return.
# 2. Find the mid index.
# 3. Call merge_sort() for left half  and right half of the array recursively.
# 4. Call merge() to merge the two sorted halves into one sorted array.


def merge(arr:list(),l:int,mid:int,r:int):

    start1=l
    start2=mid+1

    end1=mid
    end2=r

    temp=[]
    while start1<=end1 and start2<=end2:
        if arr[start1]<arr[start2]:
            temp.append(arr[start1])
            start1+=1
        else:
            temp.append(arr[start2])
            start2+=1

    while start1<=end1:
        temp.append(arr[start1])
        start1+=1

    while start2<=end2:
        temp.append(arr[start2])
        start2+=1

    for i in range(len(temp)):
        arr[l+i]=temp[i]

    



def merge_sort(arr:list(),l:int,r:int):
    if l>=r:
        return
    mid=(l+r)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)

    merge(arr,l,mid,r)



