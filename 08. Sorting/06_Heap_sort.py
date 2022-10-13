
def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[l]>arr[largest]:
        largest=l

    if r<n and arr[r]>arr[largest]:
        largest=r

    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)


def heapsort(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

    return arr



def main():
    arr=[5,4,3,2,1]
    n=len(arr)

    print("Given array is")
    print(arr)

    heapsort(arr)
    print("\nSorted array is")
    print(arr)


# main()  # uncomment this line to run the code

# Output:
# Given array is
# [5, 4, 3, 2, 1]
#
# Sorted array is
# [1, 2, 3, 4, 5]
