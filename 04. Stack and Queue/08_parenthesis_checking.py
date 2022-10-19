
# This will be updated shortly
from stack_and_queue import stack

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



st="((()))["

print(check_parenthesis(st))
