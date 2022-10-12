from stack_and_queue import stack

def prefix_evaluation(prefix):

    st=stack()

    for i in range(len(prefix)-1,-1,-1):

        if prefix[i].isdigit():
            st.push(int(prefix[i]))
        else:
            op1=st.pop()
            op2=st.pop()
            if prefix[i]=='+':
                st.push(op1+op2)
            elif prefix[i]=='-':
                st.push(op1-op2)
            elif prefix[i]=='*':
                st.push(op1*op2)
            elif prefix[i]=='/':
                st.push(op1/op2)
            elif prefix[i]=='^':
                st.push(op1**op2)

    return st.pop()


    