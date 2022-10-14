
# Problem Statement:   Given a roman numeral, convert it to an integer.

# Algorithm:

# 1. Create a dictionary with key as roman numeral and value as integer
# 2. Iterate from 0 to len(s)-1
# 3. If s[i] is not the last character and value of s[i] is less than value of s[i+1], then subtract value of s[i] from result
# 4. Else, add value of s[i] to result
# 5. Return result


# Time Complexity: O(n)
# Space Complexity: O(1)


# Roman to Integer Conversion


def roman_to_int(s):

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    for i in range(len(s)):

        if i < len(s)-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
            result -= roman_dict[s[i]]
        else:
            result += roman_dict[s[i]]

    return result



# Problem Statement:   Given an integer, convert it to a roman numeral.

# Algorithm:

# 1. Create a list of numbers and symbols in desc. order
# 2. Initialize result to empty string and i to 0
# 3. Iterate while num is > 0:
#    a. find the quoitent(q) of num divided by numbers[i] and save remainder to num
#    b. add the symbol[i] to result q times
#    c. Increment i
# 4. Return result


# Time Complexity: O(n)
# Space Complexity: O(1)


# Integer to Roman Conversion

def int_to_roman(num):

    numbers=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    result = ''

    i=0

    while num:

        a=num // numbers[i]
        num=num%numbers[i]

        result+=symbols[i] *a

        i+=1

    return result








def main():

    s = 'MCMXCIV'

    print(roman_to_int(s))

    num = 1994

    print(int_to_roman(num))





main() # Call to main()

# Output:
# 1994
# MCMXCIV