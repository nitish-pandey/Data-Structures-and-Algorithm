
from stack_and_queue import stack

# Problem Statement: Parenthesis Checking

# Given an expression string exp , write a program to examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.

# Algorithm:
# 1. Create a stack to store opening parenthesis.
# 2. Scan the given expression and do following for every scanned element.
# ……a. If the element is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
# ……b. If the element is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped element is the matching starting bracket then fine else parenthesis are not balanced.
# 3. After complete traversal, if there is some starting bracket left in stack then “not balanced”

# Time Complexity: O(n)
# Space Complexity: O(n)

def check_parenthesis(string):
    st=stack()

    for i in string:

        if i=='(':
            st.push(0)
        elif i=='{':
            st.push(1)
        elif i=='[':
            st.push(2)
        
        elif i==')':
            if st.pop() !=0:
                return False

        elif i=='}':
            if st.pop()!=1:
                return False
            
        elif i==']':
            if st.pop()!=2:
                return False

    return st.is_empty()

