
# Problem Statement: Find the nth power of x


# Approach 1: Uniform Division

# Algorithm:

# 1. If n is 0, return 1
# 2. If n is less than 0, reciporcal x and make n positive with same value
# 3. call the function recursively for n/2 (integer) and make square of ans
# 4. If n is odd, multiply ans with x
# 5. Return ans

# Time Complexity: O(logn)
# Space Complexity: O(logn)




def power_of(x,n):

    if n ==0:
        return 1

    if n<0:
        x=1/x
        n=abs(n)

    temp=power_of(x,n//2)

    temp*=temp

    if n%2==1:
        temp*=x

    return temp



# Approach 2: Uniform Decrease

# Algorithm:
# 1. If n is 0, return 1
# 2. If n is less than 0, reciporcal x and make n positive with same value
# return x * power_of(x,n-1)


# Time Complexity: O(n)
# Space Complexity: O(n)

def power_of_2nd_app(x,n):

    if n ==0:
        return 1

    if n<0:
        x=1/x
        n=abs(n)

    return x * power_of_2nd_app(x,n-1)



def main():

    x=2.1
    n=10

    print(power_of(x,n))


main()

# Output:
# 1667.988097