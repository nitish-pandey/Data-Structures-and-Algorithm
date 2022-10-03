
# Merging two sorted arrays

# Algorithm
# 1. Initialize an empty array arr3
# 2. Initialize two pointers i and j and set them to 0
# 3. Iterate until i<len(arr1) and j<len(arr2)
# 4. if arr1[i]<arr2[j] then append arr1[i] to arr3 and increment i
# 5. else append arr2[j] to arr3 and increment j
# 6. if i<len(arr1) then append arr1[i:] to arr3
# 7. if j<len(arr2) then append arr2[j:] to arr3
# 8. return arr3


# Time complexity: O(n+m)
# Space complexity: O(n+m)

def merge(arr1,arr2):
    arr3 = []
    i,j=0,0
    n,m=len(arr1),len(arr2)

    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    
    while i<n:
        arr3.append(arr1[i])
        i+=1
    
    while j<m:
        arr3.append(arr2[j])
        j+=1

    return arr3

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,21,22,23,24]
    arr2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,35,56,78,90]
    print(merge(arr1, arr2))

main() # call main function

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 35, 56, 78, 90]