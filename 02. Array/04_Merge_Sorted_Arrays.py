
# Problem Statement1: Given two sorted arrays, merge them in sorted order.
# Tags: Array, Two Pointers Approach

# Algorithm:

# 1. Initialize new array arr3 of size n+m
# 2. Initialize i=0, j=0 and k=0    
# 3. Iterate while i<n and j<m
# 4. If arr1[i]<arr2[j] then arr3[k]=arr1[i] and increment i and k
# 5. Else arr3[k]=arr2[j] and increment j and k
# 6. Iterate while i<n
# 7. arr3[k]=arr1[i] and increment i and k
# 8. Iterate while j<m
# 9. arr3[k]=arr2[j] and increment j and k
# 10. Return arr3


# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

def merge_sorted_arrays(arr1,arr2):

    n=len(arr1)
    m=len(arr2)

    arr3=[0]*(n+m)

    i=0
    j=0
    k=0

    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            i+=1
        else:
            arr3[k]=arr2[j]
            j+=1
        k+=1    

    while i<n:
        arr3[k]=arr1[i]
        i+=1
        k+=1

    while j<m:
        arr3[k]=arr2[j]
        j+=1
        k+=1

    return arr3



# Problem Statement 2: Intersection of 2 sorted arrays



def intersection_of_two_sorted_arrays(arr1:list(),arr2:list()) ->list():
    n=len(arr1)
    m=len(arr2)

    arr3=[0]*(n+m)

    i=0
    j=0
    k=0

    while i<n and j<m:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            arr3[k]=arr1[i]
            i+=1
            j+=1
            k+=1

    return arr3[:k]




# Problem Statement 3: Union of 2 sorted arrays


def union_of_two_sorted_arrays(arr1:list(),arr2:list()) ->list():

    n=len(arr1)
    m=len(arr2)

    arr3=[0]*(n+m)

    i=0
    j=0
    k=0

    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            i+=1
        elif arr1[i]>arr2[j]:
            arr3[k]=arr2[j]
            j+=1
        else:
            arr3[k]=arr1[i]
            i+=1
            j+=1
        k+=1

    while i<n:
        arr3[k]=arr1[i]
        i+=1
        k+=1

    while j<m:
        arr3[k]=arr2[j]
        j+=1
        k+=1

    return arr3[:k]

