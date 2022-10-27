

# Problem Statement: Given an array of integers nums, sort the array in ascending order using Quick Sort Algorithm.


# Approach: We will use Divide and Conquer Algorithm to solve this problem.
#           We will choose a pivot element and partition the array around the pivot element.
#           Then we will sort the left half and right half of the array recursively.


# Time Complexity: O(nlogn) in average case and O(n^2) in worst case.
# Space Complexity: O(n) in average case and O(n^2) in worst case.


# Algorithm:



def partition(arr,l,r):

    pivot=arr[r]
    ind=l-1

    for i in range(l,r):
        if arr[i]<pivot:
            ind+=1
            arr[ind],arr[i]=arr[i],arr[ind]

    arr[ind+1],arr[r]=arr[r],arr[ind+1]

    return ind+1



def quick_sort(arr,l,r):

    if l>=r:
        return

    pivot=partition(arr,l,r)

    quick_sort(arr,l,pivot-1)
    quick_sort(arr,pivot+1,r)

