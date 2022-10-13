

# This function is used to convert a string to an integer
# without using the built-in function int().
# The function takes a string as an argument and returns an integer.


# Time complexity: O(n)
# Space complexity: O(1)

def atoi(s):
    num = 0
    for i in s:
        num = num * 10 + ord(i) - ord('0')
    return num


def main():
    s = "123"
    print(atoi(s))


main() # Call the main function

# Output
# 123
