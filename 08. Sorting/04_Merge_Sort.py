
# Problem Statement: Sort a list of numbers using merge sort

# Algorithm:

# 1. Divide the list into two halves
# 2. Sort the first half
# 3. Sort the second half
# 4. Merge the two halves

# Time Complexity: O(nlogn)
# Space Complexity: O(n)


def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)


        
    return arr


def merge(arr,l,p,r):

    n1 = p - l + 1
    n2 = r - p

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[p + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def main():

    arr = [64, 25, 12, 22, 11]
    print(merge_sort(arr))



main() # Call to main() function


# Output:
# [11, 12, 22, 25, 64]
