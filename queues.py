class Node:
    def __init__(self, data, next=None) -> None:
        self.__data = data
        self.__next = next

    def __str__(self) -> str:
        return f"{self.__data}"

    def set_data(self, value):
        self.__data = value

    def set_next(self, node):
        self.__next = node

    def data(self):
        return self.__data
    
    def next(self):
        return self.__next
    
    def has_next(self):
        if self.__next:
            return True
        return False
    

class Queue:
    def __init__(self, head=None) -> None:
        self.__head = head
        self.__size = 0

    def __str__(self) -> str:
        string = "-----[ Front ]-----\n"
        if self.__head:
            current = self.__head
            while current.has_next():
                string = f"{string}{current}\n"
                current = current.next()
            string = f"{string}{current}"
        else:
            string = "Empty queue."
        return string
    
    def size(self):
        return self.__size

    def queue(self, data):
        if self.__head:
            current = self.__head
            while current.has_next():
                current = current.next()
            current.set_next(Node(data))
        else:
            self.__head = Node(data)
        self.__size += 1

    def dequeue(self):
        if self.__head:
            if self.__head.has_next():
                self.__head = self.__head.next()
            else: 
                self.__head = None
        self.__size -= 1