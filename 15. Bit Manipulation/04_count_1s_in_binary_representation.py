
# Problem Statement: Count the number of 1s in the binary representation of a number

# Algorithm:
# 1. If the number is 0, then return 0
# 2. If the number is not 0, then count the number of 1s in the binary representation of the number
# 3. The number of 1s in the binary representation of the number is equal to the number of times we can perform the operation num=num & (num-1)
# 4. Return the count

# Time Complexity: O(logn)
# Space Complexity: O(1)


def count_1s(num):

    count=0

    while num:

        count+=1

        num=num & (num-1)

    return count


