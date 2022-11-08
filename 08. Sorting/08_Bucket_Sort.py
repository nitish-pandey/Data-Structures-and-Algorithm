

# Problem Statement: Sort the given array of Floating numbers using Bucket Sort

# Bucket Sort is used to sort array of floating point values



def insertionSort(arr):
    n=len(arr)

    if n<2:
        return
    
    for i in range(1,n):
        j=i

        while j>0 and arr[j-1]>arr[j]:
            # swap arr[j] and arr[j-1]
            arr[j],arr[j-1]=arr[j-1],arr[j]


    



def bucket_sort(arr):

    n=len(arr)

    buckets=[[] for _ in range(10)]

    for i in arr:

        a=int(i*10)
        buckets[a].append(i)

    
    for bucket in buckets:
        insertionSort(bucket)

    arr=[]

    for bucket in buckets:
        for i in bucket:
            arr.append(i)

    return arr
    

arr=[0.9,0.3,0.5,0.1,0.6,0.68,0.65]


arr=bucket_sort(arr)

print(arr)