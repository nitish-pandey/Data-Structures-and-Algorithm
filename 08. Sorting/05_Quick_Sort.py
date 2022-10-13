

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def main():
    arr = [5, 4, 3, 2, 1]

    print("Given array is")
    print(arr)

    print("\nSorted array is")
    print(quick_sort(arr))


# main()  # uncomment this line to run the code

# Output:
# Given array is
# [5, 4, 3, 2, 1]
#
# Sorted array is
# [1, 2, 3, 4, 5]
