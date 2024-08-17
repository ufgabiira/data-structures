class Node:
    def __init__(self, data, next=None) -> None:
        self.__data = data
        self.__next = next

    def __str__(self) -> str:
        return f"{self.__data}"
    
    def next(self):
        return self.__next
    
    def set_next(self, node) -> None:
        self.__next = node

    def has_next(self) -> bool:
        if self.__next:
            return True
        else:
            return False
    
    def data(self):
        return self.__data

    def set_data(self, data) -> None:
        self.__data = data


class LinkedList:
    def __init__(self, head=None) -> None:
        self.__head = head
        self.__size = 0

    def __str__(self) -> str:
        if self.__size == 0:
            return ("List is empty.")
        current = self.__head
        i = 0
        string = ""
        while current.has_next():
            string = f"{string}({i}, {current}) => "
            current = current.next()
            i += 1
        string = f"{string}({i}, {current})"
        return string
    
    def size(self):
        return self.__size
    
    def add(self, data, index=None) -> None:
        self.__size += 1
        if index and (index >= self.__size):
            raise IndexError
        elif self.__head is None:
            self.__head = Node(data)
        elif index == 0:
            new_node = Node(data, next=self.__head)
            self.__head = new_node
        elif index is None:
            current = self.__head
            while current.has_next():
                current = current.next()
            current.set_next(Node(data))
        else:
            current = self.__head
            i = 0
            while current.has_next():
                if i == index-1:
                    new_node = Node(data, next=current.next())
                    current.set_next(new_node)
                    return
                else:
                    i += 1
                    current = current.next()

    def remove(self, index=None) -> None:
        if self.__size == 0 or self.__head is None: # no elements
            raise Exception("List is empty of head is not defined.")
        elif index == 0 or not self.__head.has_next(): # remove first
            self.__head = self.__head.next()        
        elif index > self.__size or index < 0: # index out of bounds
            raise IndexError(f"Index {index} out of bounds. List has {self.__size} elements.")
        elif index is None or index == self.__size-1: # remove last element
            current = self.__head
            while current.next().has_next():
                current = current.next()
            current.set_next(None)
        else: # remove middle elements
            current = self.__head.next()
            previous = self.__head
            i = 1
            while current.has_next():
                if i == index:
                    previous.set_next(current.next())
                    break
                else:
                    i += 1
                    current = current.next()
                    previous = previous.next()
        self.__size -= 1

    def get(self, index):
        current = self.__head
        i = 0
        while current.has_next():
            if i == index:
                return current
            else:
                current = current.next()
                i += 1
        return current