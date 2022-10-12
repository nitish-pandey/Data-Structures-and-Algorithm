

class BST:

    class node:
        def __init__(self, value,hd=0):
            self.value = value
            self.left = None
            self.right = None
            self.hd = hd

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.root = None

    
    def __insert(self,root,value,hd):

        if not root:
            return self.node(value,hd)

        if value < root.value:
            root.left = self.__insert(root.left,value,hd-1)

        else:
            root.right = self.__insert(root.right,value,hd+1)

        return root

    
    def insert(self, value):

        self.root = self.__insert(self.root,value,0)
        return

    def search(self, value):

        if self.root is None:
            return False

        current = self.root

        while current is not None:

            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    