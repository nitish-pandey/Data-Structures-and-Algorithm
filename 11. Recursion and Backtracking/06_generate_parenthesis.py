

# Problem Statement: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Time Complexity: O(2^n)

# Space Complexity: O(n)

# Algorithm: We will use recursion and backtracking to solve this problem. 
#               We will start with an empty string and keep adding '(' and ')' to it. 
#               We will keep track of the number of open and close brackets we have added. 
#               We will add '(' only if the number of open brackets is less than n. We will add ')' only if the number of close brackets is less than the number of open brackets. 
#               We will stop adding brackets when the length of the string is 2*n.


class parenthesis:

    def __init__(self) -> None:
        self.ans=[]
        pass

    def __generator(self,st,open,close):
        if open==close==self.n:
            self.ans.append(st)
            return
        
        if open<self.n:
            self.__generator(st+'(',open+1,close)

        
        if close<open:
            self.__generator(st+')',open,close+1)


    
    def generate(self,n):
        self.ans=[]
        self.n=n

        self.__generator("",0,0)

        return self.ans




def main():

    n=3

    par=parenthesis()

    ans=par.generate(n)

    print(ans)



# main() # calling main function


# Output:
# ['((()))', '(()())', '(())()', '()(())', '()()()']