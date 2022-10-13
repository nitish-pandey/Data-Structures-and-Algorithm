

class priority_queue:

    def __init__(self):
        self.heap = []

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):

        parent = (index - 1) // 2

        if index <= 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    
    def __bubble_down(self, index):

        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)


    def __str__(self):

        return str(self.heap)

    def __len__(self):

        return len(self.heap)

    def is_empty(self):

        return len(self.heap) == 0

    def remove(self, item):

        for i, x in enumerate(self.heap):
            if x == item:
                self.__swap(i, len(self.heap) - 1)
                self.heap.pop()
                self.__bubble_down(i)
                break

    def heapify(self, list):

        self.heap = list
        for i in range(len(list) - 1, -1, -1):
            self.__bubble_down(i)

    def heap_sort(self, list): 

        self.heapify(list)
        sorted_list = []

        for i in range(len(self.heap)):
            sorted_list.append(self.extract_max())

        return sorted_list

    def insert(self, item):
        self.heap.append(item)
        self.__float_up(len(self.heap) - 1)


    def get_max(self):

        if self.heap[0]:
            return self.heap[0]
        else:
            return False


    def extract_max(self):

        if len(self.heap) > 0:
            self.__swap(0, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubble_down(0)
        else:
            max = False

        return max

    