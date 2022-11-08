
# Problem Statement: Sort the given array using radix sort

# Approach:
# We will sort the array begining from ones place to maximum place value using count sort and keeping relative position same

# Algorithm:
# 1. Get the length of Maximum element of array
# 2. Apply the count Sort from 0th digit( ones place) to Maximum length digit


# For Algorithm of Count Sort: Refer to 09_Count_sort.py in this same folder
# Here, Count sort is changed for ith digit sorting 


# Time Complexity: O(len(A[i]) * n)


def get_ith_digit(num, i):

    p=10** i

    return (num//p) %10



def count_sort(arr,k):

    count_arr=[0]*10
    n=len(arr)

    for num in arr:

        a=get_ith_digit(num,k)
        count_arr[a]+=1


    for i in range(1,10):
        count_arr[i]+=count_arr[i-1]

    ans=[0]*n
    
    for i in range(n-1,-1,-1):

        a=get_ith_digit(arr[i],k)
        count_arr[a]-=1
        ans[count_arr[a]]=arr[i]


    return ans


def radix_sort(arr):

    m=max(arr)
    l=len(str(m))

    for i in range(0,m+1):

        arr=count_sort(arr,i)

    return arr


def main():

    arr=[23,56,24,78,109,89,3,98]

    arr=radix_sort(arr)

    print(arr)



main() # call to main function


# Output:
# [3, 23, 24, 56, 78, 89, 98, 109]


# Radix Sort is stable sort algorithm.
# It is not In-Place (requires extra space).
# It is non-comparision based algorithm.