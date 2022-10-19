

# Problem Statement: Binary search

# Algorithm:
# 1. Find the middle element
# 2. If the middle element is the element to be searched, return the index
# 3. If the middle element is greater than the element to be searched, then search in the left half
# 4. If the middle element is smaller than the element to be searched, then search in the right half


# Time Complexity: O(logn)
# Space Complexity: O(1)


def binary_search_iterative(arr,element):

    start=0
    end=len(arr)-1

    while start<=end:

        mid=(start+end)//2

        if arr[mid]==element:
            return mid

        elif arr[mid]>element:
            end=mid-1

        else:
            start=mid+1

    return -1



# Problem Statement: Binary Search using recursion

# Algorithm:
# 1. If start greater than end, return "Not Found"
# 2. Find the mid index i.e. (start+end)//2
# 3. If the element at mid index is equal to the key, return the mid index
# 4. If the mid element is greater than key, recursively call the function by changing end to mid-1 and return
# 5. Else, recursively call by changing start to mid+1 and return

# Time Complexity: O(logn)
# Space Complexity: O(logn) # due to call-stack


def binary_search_recursive(arr,element,start,end):

    if start>end:
        return -1

    mid=(start+end)//2

    if arr[mid]==element:
        return mid

    elif arr[mid]>element:
        return binary_search_recursive(arr,element,start,mid-1)

    else:
        return binary_search_recursive(arr,element,mid+1,end)


