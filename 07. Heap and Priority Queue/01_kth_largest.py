

def heapify(arr,n,ind):

    curr=ind

    while curr<n:
        l=curr*2+1
        r=curr*2+2
        large=curr

        if l<n and arr[l]>arr[large]:
            large=l
        if r<n and arr[r]>arr[large]:
            large=r

        if large !=curr:
            arr[large],arr[curr]=arr[curr],arr[large]
            curr=large
        else:
            break
    


def kth_largest(arr,k):

    n=len(arr)

    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,n-1-k,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

    return arr[n-k]



def main():

    arr=[4,2,9,7,5,6,7,1,3]
    k=4

    print(kth_largest(arr,k))



main() # calling the  main function

# Output:

# 6