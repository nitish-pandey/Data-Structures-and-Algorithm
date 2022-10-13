
from stack_and_queue import stack


# Problem Statement: Convert an infix expression to a prefix expression

# Algorithm:

# 1. Reverse the infix expression
# 2. Scan the reversed infix expression from left to right
# 3. If the scanned character is an operand, append it to the prefix expression
# 4. If the scanned character is an operator, push it to the stack
# 5. If the scanned character is an opening parenthesis, pop the stack until the corresponding closing parenthesis is found
# 6. Repeat steps 2-5 until the end of the expression is reached
# 7. Pop all the elements from the stack and append them to the prefix expression

# Time Complexity: O(n)
# Space Complexity: O(n)


def infix_to_prefix(exp):

    exp = exp[::-1]
    s = stack()
    prefix = ""

    for i in range(len(exp)):
        if exp[i].isalpha():
            prefix += exp[i]
        elif exp[i] == ")":
            s.push(exp[i])
        elif exp[i] == "(":
            while s.peek() != ")":
                prefix += s.pop()
            s.pop()
        else:
            while not s.is_empty() and precedence(exp[i]) <= precedence(s.peek()):
                prefix += s.pop()
            s.push(exp[i])

    while not s.is_empty():
        prefix += s.pop()

    return prefix[::-1]




# Problem Statement: Convert an infix expression to a postfix expression

# Algorithm:

# 1. Scan the infix expression from left to right
# 2. If the scanned character is an operand, append it to the postfix expression
# 3. If the scanned character is an operator, push it to the stack
# 4. If the scanned character is an opening parenthesis, push it to the stack
# 5. If the scanned character is an closing parenthesis, pop the stack until the corresponding opening parenthesis is found
# 6. Repeat steps 2-5 until the end of the expression is reached
# 7. Pop all the elements from the stack and append them to the postfix expression

# Time Complexity: O(n)
# Space Complexity: O(n)


def infix_to_postfix(exp):

    s = stack()
    postfix = ""

    for i in range(len(exp)):
        if exp[i].isalpha():
            postfix += exp[i]
        elif exp[i] == "(":
            s.push(exp[i])
        elif exp[i] == ")":
            while s.peek() != "(":
                postfix += s.pop()
            s.pop()
        else:
            while not s.is_empty() and precedence(exp[i]) <= precedence(s.peek()):
                postfix += s.pop()
            s.push(exp[i])

    while not s.is_empty():
        postfix += s.pop()

    return postfix


# Precedence of operators
# ^ = 3
# * = 2
# / = 2
# + = 1
# - = 1

def precedence(op):

    if op == "^":
        return 3
    elif op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    else:
        return 0



def main():

    exp = "a+b*(c^d-e)^(f+g*h)-i"
    print("Infix expression: ", exp)
    print("Prefix expression: ", infix_to_prefix(exp))
    print("Postfix expression: ", infix_to_postfix(exp))



main() # Call to main() function


# Output:
# Infix expression:  a+b*(c^d-e)^(f+g*h)-i
# Prefix expression:  -+a^*b-cde^fgh*+i
# Postfix expression:  abcd^e-fgh*+^*+i-

