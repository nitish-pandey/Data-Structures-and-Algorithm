

def first_and_last_position(arr,k):

    n=len(arr)

    start=0
    end=n-1

    first=-1

    while start<=end:
        mid=(start+end)//2

        if arr[mid]==k:
            first=mid
            end=mid-1
        
        elif arr[mid]>k:
            end=mid-1

        else:
            start=mid+1

    
    start=first+1
    end=n-1
    last=first

    while start<=end:
        mid=(start+end)//2

        if arr[mid]==k:
            last=mid
            start=mid+1

        elif arr[mid]>k:
            end=mid-1
        else:
            start=mid+1



    return first,last




arr=[1,2,3,4,4,4,5,6,7,8,9,9,9]

print(first_and_last_position(arr,4))
