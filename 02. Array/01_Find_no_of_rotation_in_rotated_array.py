
# rotating the array  k-times anti-clockwise
def rotate_by_k(arr,k):
    n=len(arr)
    if n<=1:
        return arr
    k=k%n
    arr=arr[n-k:]+arr[:n-k]
    return arr
    
#  finding the no. of rotation in rotated array anti-clockwise


# Algorithm
# 1. Initialize start=0 and end=n-1
# 2. If arr[0]<arr[n-1] then return 0
# 3. Iterate until start<=end
# 4. mid=start+(end-start)//2
# 5. If arr[mid]>arr[mid+1] then return mid+1
# 6. If arr[mid]<arr[mid-1] then return mid
# 7. If arr[mid]>arr[0] then start=mid+1
# 8. Else end=mid-1
# 9. return 0

#  Time complexity: O(logn)
#  Space complexity: O(1)

def find_no_of_rot(arr):

    n=len(arr)
    if n<=1:
        return 0
    
    if arr[0]<arr[n-1]:
        return 0

    start=0
    end=n-1

    while start<=end:
        mid=start+(end-start)//2

        if mid<n-1 and arr[mid]>arr[mid+1]:
            return mid+1
        elif mid>0 and arr[mid]<arr[mid-1]:
            return mid

        if arr[mid]>arr[0]:
            start=mid+1
        else:
            end=mid-1
    return 0


def main():
    arr=[1,2,3,4,5,6,7,8,9] 
    arr=rotate_by_k(arr,3)
    print(find_no_of_rot(arr))



main() # call main function

# output
# 3

#changes made git