
# Problem statement: Sort a list of numbers using quick sort


# Algorithm:

# 1. If the left index is less than the right index, call the partition function
# 2. Set the pivot index to the return value of the partition function
# 3. Call the quick sort function recursively using the left index and the pivot index-1 as the left and right indices
# 4. Call the quick sort function recursively using the pivot index+1 and the right index as the left and right indices
# 5. Return the sorted array

# Time Complexity: O(nlogn)
# Space Complexity: O(1)


def quick_sort(arr,l,r):

    if l>=r:
        return 

    pivot=partition(arr,l,r)

    quick_sort(arr,l,pivot-1)
    quick_sort(arr,pivot+1,r)





# Problem Statement: Partition an array around a pivot element

# Algorithm:

# 1. Set the pivot to the last element of the array
# 2. Set i to the index of the first element of the array
# 3. Iterate through the array using a for loop using j as the index
# 4. If the element at index j is less than the pivot, swap the elements at index i and j and increment i
# 5. Swap the elements at index i and the pivot
# 6. Return the index of the pivot

# Time Complexity: O(n)
# Space Complexity: O(1)


def partition(arr,l,r):

    pivot=arr[r]
    i=l

    for j in range(l,r):

        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1

    arr[i],arr[r]=arr[r],arr[i]

    return i





def main():

    arr = [64, 25, 12, 22, 11]
    quick_sort(arr,0,len(arr)-1)
    print(arr)


main() # Call to main() function

# Output:

# [11, 12, 22, 25, 64]