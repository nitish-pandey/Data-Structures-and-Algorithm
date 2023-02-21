from stack_and_queue import stack


# Problem Statement: You are given a string, remove the outer parenthesis.

# For example: (A) gives A, (()) gives (), (abc) gives abc, (()()) gives ()()

# Tags: Stack

# Algorithm:
# 1. Initialize the empty stack and ans string variable
# 2. Iterate over the string:
# 3.    If the character is '(':
# 4.        If the stack is empty, add the character to ans
# 5.        Add the character to stack
# 6.    else pop the stack
# 7.        if stack is not empty, add the character to ans
# 9. return ans

# Time complexity: O(n)
# Space complexity: O(n)


def remove_outer_parenthesis(string:str)->str:

    ans=""
    st=stack()

    for c in string:

        if c=='(':

            if st.isEmpty():
                ans+=c

            st.push(c)

        else:
            st.pop()

            if not st.isEmpty():
                ans+=c

    return ans


    