
# Problem Statement: You are given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Example:
# Input: s = "egg", t = "add"

# Tags: Hashing

# Algorithm:
# 1. Create two hash table, h1 and h2
# 2.Iterate over the string s and t
# 3. If the character s[i] is not present in h1 and t[i] is not present in h2, then add the character to the hash table
# 4. If character S[i] in presnt in h1 and t[i] is not present in h2, or vice-versa then return False
# 5. Check if the character in h1 and h2 are same, if not return False
# 6. Return True at the end

# Time Complexity: O(n)
# Space Complexity: O(n)

def isomorphic_string(s:str,t:str) -> bool:

    h1={}
    h2={}

    for i in range(len(s)):

        if s[i] not in h1 or t[i] not in h2:

            if s[i] in h1 or t[i] in h2:
                return False
            
            h1[s[i]]=t[i]
            h2[t[i]]=s[i]

        elif h1[s[i]]!=t[i] or h2[t[i]]!=s[i]:
            return False

    return True



# <-- End of Code -->


def main():

    s="egg"
    t="add"

    print(isomorphic_string(s,t))



main() # calling to main funtion

# Output: True