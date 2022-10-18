
# Problem Statement: Check if the number is power of two or not using bit manipulation

# Algorithm:
# 1. If the number is 0, then it is not a power of two
# 2. If the number is power of two, then the number and the number-1 will be 0

# Time Complexity: O(1)
# Space Complexity: O(1)


def check_if_power_of_two(num):
    if num ==0:
        return False

    return (num & (num-1)) == 0



