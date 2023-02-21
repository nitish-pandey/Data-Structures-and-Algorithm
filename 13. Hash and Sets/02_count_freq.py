from collections import defaultdict

# Problem Statement: You are given a array, find the frequency of all elements

# Algorithm:
# 1. Create a hash-map i.e. dictionary
# 2. Iterate over the elements and increase its count



def count_freq(arr:list):

    hash_map=defaultdict(int)

    for i in arr:
        hash_map[i]+=1


    print(hash_map)




