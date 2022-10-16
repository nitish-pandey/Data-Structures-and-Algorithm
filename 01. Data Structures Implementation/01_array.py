
#  Array Data Structure is a collection of items stored at contiguous memory locations. 
#       The idea is to store multiple items of the same type together. 
#       This makes it easier to calculate the position of each element by simply adding an offset to a base value, 
#       i.e., the memory location of the first element of the array (generally denoted by the name of the array).

# Advantages:
# 1. Fast lookups
# 2. Fast push/pop
# 3. Ordered
# 4. Flexible size

# Disadvantages:
# 1. Slow inserts
# 2. Slow deletes
# 3. Fixed size



class array:

    def __init__(self) -> None:
        self.__arr=[]*1000 
        self.__n=0
        pass

    def append(self,a):
        self.__arr[self.__n]=a
        self.__n+=1
    
    def pop(self):
        if self.__n==0:
            return
        self.__n-=1
        return self.__arr[self.__n]

    def print(self):

        n=self.__n
        if n==0:
            print("Array is empty")
            return 
        
        print("Array is : ")
        print(self.__arr[:n])