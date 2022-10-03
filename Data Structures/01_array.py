
#  Array Data Structure


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