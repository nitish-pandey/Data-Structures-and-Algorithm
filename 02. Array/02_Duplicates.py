
# find duplicates in n time complexity and n space complexity


# Algorithm
# 1. Initialize s=set() and dup=[]
# 2. Iterate through arr
# 3. If i in s then append i to dup
# 4. Else add i to s
# 5. return dup

# Time complexity: O(n)
# Space complexity: O(n)

def find_duplicates(arr):
    n=len(arr)
    if n<=1:
        return []
    s=set()
    dup=[]

    for i in arr:
        if i in s:
            dup.append(i)
        else:
            s.add(i)
    return dup

def main():
    arr=[1,2,4,5,6,7,8,9,3,4,5,6,7,8,9,100]
    ans=find_duplicates(arr)
    print(ans)


main() # call main function

# output
# [4, 5, 6, 7, 8, 9]