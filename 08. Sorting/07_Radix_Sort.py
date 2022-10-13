

def radix_sort(arr):
    max_len = len(str(max(arr)))
    for i in range(max_len):
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[num // (10 ** i) % 10].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr



def main():
    arr = [5, 4, 3, 2, 1]

    print("Given array is")
    print(arr)

    print("\nSorted array is")
    print(radix_sort(arr))


# main()  # uncomment this line to run the code

# Output:
# Given array is
# [5, 4, 3, 2, 1]
#
# Sorted array is
# [1, 2, 3, 4, 5]
