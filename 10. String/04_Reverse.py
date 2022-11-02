

def reverse_string(st:str) ->str:

    curr=""

    for i in st:
        curr=i+curr

    return curr


def reverse_each_word(st:str) -> str:

    ans=""
    curr=" "

    for i in st:
        if i==' ':
            ans+=curr
            curr=" "

        else:
            curr=i+curr

    return ans+curr


def main():

    st="hello world , I am a small program"


    print(reverse_each_word(st))
    print(reverse_string(st))



# main()