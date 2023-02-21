
# Hashing is the process of mapping a given value with a particular key for faster access of elements. 
# Hashing doesn’t allow duplicate elements. 
# It stores the key-value pair but the key is generated through a hashing function.


hash_table = [None] * 10

def hash_function(key):
    return key % 10


def insert(hash_table, key, value):
    hash_key = hash_function(key)
    hash_table[hash_key] = value




def search(hash_table, key):
    hash_key = hash_function(key)
    return hash_table[hash_key]


def delete(hash_table, key):
    hash_key = hash_function(key)
    hash_table[hash_key] = None


    
def main():

    insert(hash_table, 10, 'Nepal')
    insert(hash_table, 25, 'India')
    insert(hash_table, 20, 'USA')
    insert(hash_table, 9, 'China')
    insert(hash_table, 21, 'Russia')
    insert(hash_table, 21, 'Russia')

    print(hash_table)

    print(search(hash_table, 10))
    print(search(hash_table, 25))

    delete(hash_table, 10)

    print(hash_table)

    print(search(hash_table, 10))




main() # call main function


# Output:
# ['USA', 'Russia', None, None, None, 'India', None, None, None, 'China']
# USA
# India
# [None, 'Russia', None, None, None, 'India', None, None, None, 'China']
# None

