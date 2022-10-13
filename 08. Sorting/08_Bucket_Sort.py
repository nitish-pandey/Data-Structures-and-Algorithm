
def Bucket_Sort(arr):
    n=len(arr)

    if n<=1:
        return arr

    max=arr[0]
    min=arr[0]

    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]

    bucket=[[] for i in range(max-min+1)]

    for i in range(n):
        bucket[arr[i]-min].append(arr[i])

    arr=[]

    for i in range(max-min+1):
        arr+=bucket[i]

    return arr


def main():
    arr=[5,4,3,2,1]
    
    print("Given array is")
    print(arr)
    
    print("\nSorted array is")
    print(Bucket_Sort(arr))


# main()  # uncomment this line to run the code

# Output:
# Given array is
# [5, 4, 3, 2, 1]
#
# Sorted array is
# [1, 2, 3, 4, 5]
