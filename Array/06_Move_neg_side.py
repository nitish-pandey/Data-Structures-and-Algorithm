
# moving the -ve elements in one side

# Algorithm:
# 1. Initialize i=0 and j=n-1
# 2. Iterate while i<j
# 3. If arr[i]<0 and arr[j]<0 then i+=1
# 4. If arr[i]>0 and arr[j]<0 then swap arr[i] and arr[j] and i+=1 and j-=1
# 5. If arr[i]>0 and arr[j]>0 then j-=1
# 6. Else i+=1 and j-=1
# 7. return arr

# Time complexity: O(n)
# Space complexity: O(1)

def move_neg(arr):
    n=len(arr)
    if n<=1:
        return arr
    i=0
    j=n-1
    while i<j:
        if arr[i]<0 and arr[j]<0:
            i+=1
        elif arr[i]>0 and arr[j]<0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i]>0 and arr[j]>0:
            j-=1
        else:
            i+=1
            j-=1
    return arr


def main():
    arr=[-1,2,-3,4,5,6,-7,8,9]
    print(move_neg(arr))


main() # call main function

# output
# [-1, -3, -7, 4, 5, 6, 2, 8, 9]
