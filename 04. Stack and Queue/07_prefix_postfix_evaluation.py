from stack_and_queue import stack


# Problem Statement: Evaluate a prefix expression

# Algorithm:

# 1. Scan the expression from right to left
# 2. If the scanned character is an operand, push it to the stack
# 3. If the scanned character is an operator, pop two elements from the stack
# 4. Perform the operation and push the result back to the stack
# 5. Repeat steps 2-4 until the end of the expression is reached
# 6. Return the top element of the stack

# Time Complexity: O(n)
# Space Complexity: O(n)

def prefix_evaluation(exp):

    s = stack()
    for i in range(len(exp)-1, -1, -1):
        if exp[i].isdigit():
            s.push(exp[i])
        else:
            op1 = s.pop()
            op2 = s.pop()
            if not op1 or not op2:
                print("Invalid expression")
                return None
            s.push(str(eval(op1 + exp[i] + op2)))

    return s.pop()



# Problem Statement: Evaluate a postfix expression

# Algorithm:

# 1. Scan the expression from left to right
# 2. If the scanned character is an operand, push it to the stack
# 3. If the scanned character is an operator, pop two elements from the stack
# 4. Perform the operation and push the result back to the stack
# 5. Repeat steps 2-4 until the end of the expression is reached
# 6. Return the top element of the stack

# Time Complexity: O(n)
# Space Complexity: O(n)

def postfix_evaluation(exp):

    s = stack()
    for i in range(len(exp)):
        if exp[i].isdigit():
            s.push(exp[i])
        else:
            op2 = s.pop()
            op1 = s.pop()
            if not op2 or not op1:
                print ("Invalid expression")
                return None
            
            s.push(str(eval(op1 + exp[i] + op2)))

    return s.pop()


def main():

    exp = "*+235"
    print(prefix_evaluation(exp))

    exp = "623+*"
    print(postfix_evaluation(exp))


main() # Call to main function

# Output:
# 25
# 30
