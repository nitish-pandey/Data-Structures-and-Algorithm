
# Problem Statement: You are given two strings s and t, determine if they are valid anagrams or not.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Tags: hashing

# Algorithm:
# 1. Create a hash table or count array
# 2. Iterate over string s and increment the count of the character in the hash table
# 3. Iterate over string t and decrement the count of the character in the hash table
# 4. If the count of any character is not zero, then return False

# Time Complexity: O(n)
# Space Complexity: O(n)

def valid_anagrams(s:str,t:str) -> bool:

    count=[0]*26

    for i in s:
        curr=ord(i)-ord('a')
        count[curr]+=1

    for i in t:
        curr=ord(i)-ord('a')
        count[curr]-=1

    for i in count:
        if i !=0:
            return False

    return True

# <-- End of Code -->


def main():

    s="anagram"
    t="nagaram"

    print(valid_anagrams(s,t))



main() # calling to main funtion

# Output:
# True