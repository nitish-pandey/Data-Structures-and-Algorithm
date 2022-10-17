
# Problem Statement: Sort a list of numbers using merge sort

# Algorithm:

# 1. Divide the list into two halves
# 2. Sort the first half
# 3. Sort the second half
# 4. Merge the two halves

# Time Complexity: O(nlogn)
# Space Complexity: O(n)


def merge_sort(arr,l,r):
    
    if l>=r:
        return 

    mid=(l+r)//2

    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)

    merge(arr,l,mid,r)



# Function to merge two sorted arrays

# Algorithm:

# 1. Create two arrays L and R
# 2. Copy the elements of the left half of the array into L and the elements of the right half into R
# 3. Initialize i to 0, j to 0 and k to l
# 4. Iterate through the arrays L and R using while loops
# 5. If the element at index i of L is less than or equal to the element at index j of R, copy the element at index i of L into the array at index k and increment i and k
# 6. Else, copy the element at index j of R into the array at index k and increment j and k
# 7. Copy the remaining elements of L into the array
# 8. Copy the remaining elements of R into the array



def merge(arr,l,mid,r):

    n1=mid-l+1
    n2=r-mid

    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=arr[l+i]

    for j in range(n2):
        R[j]=arr[mid+1+j]

    i=0
    j=0
    k=l

    while i<n1 and j<n2:

        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1

        k+=1

    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1




def main():

    arr = [64, 25, 12, 22, 11]
    merge_sort(arr,0,len(arr)-1)
    print(arr)


main() # Call to main() function

# Output:
# [11, 12, 22, 25, 64]