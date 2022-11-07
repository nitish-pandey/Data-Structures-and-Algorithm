

# Problem Statement: Remove adjacent duplicates from a string


# Approach: Compare the current character with the previous character. If they are same, then remove the current character. Else, move to the next character.

# Algorithm:
# 1. If the length of the string is 0 or 1, then return the string
# 2. If the first character is same as the second character, then remove the first character and call the function recursively
# 3. Else, return the first character and call the function recursively

# Time Complexity: O(n)
# Space Complexity: O(n)

def remove_adjacent_duplicates(s):

    if len(s)<2:
        return s


    if s[0]==s[1]:
        return remove_adjacent_duplicates(s[1:])

    return s[0]+remove_adjacent_duplicates(s[1:])




def main():

    s="aaabbbcc"
    print(remove_adjacent_duplicates(s))


main() # Call to main function

# Output:
# abc