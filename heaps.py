class _Node:
    def __init__(self, data, priority, next=None) -> None:
        self.__data = data
        self.__priority = priority
        self.__next = next

    def __str__(self) -> str:
        return f"{self.__data}"

    def set_data(self, value):
        self.__data = value

    def set_next(self, node):
        self.__next = node

    def set_priority(self, priority):
        self.__priority = priority

    def data(self):
        return self.__data
    
    def priority(self):
        return self.__priority
    
    def next(self):
        return self.__next
    
    def has_next(self):
        if self.__next:
            return True
        return False
    

class Heap:
    def __init__(self, head=None) -> None:
        self.__head = head
        self.__size = 0

    def __str__(self) -> str:
        string = ""
        if self.__head:
            current = self.__head
            while current.has_next():
                string = f"{string}({current.priority()}: {current}) >> "
                current = current.next()
            string = f"{string}({current.priority()}: {current})"
        else:
            string = "Empty heap."
        return string
    
    def size(self):
        return self.__size

    def hqueue(self, data, priority):
        if self.__head is None:
            self.__head = _Node(data, priority)
        else:
            current = self.__head
            while current.has_next():
                if current.priority() <= priority:
                    if current.next().priority() > priority:
                        node = _Node(data, priority, current.next())
                        current.set_next(node)
                        return
                current = current.next()
            current.set_next(_Node(data, priority))
        self.__size += 1

    def hdequeue(self):
        if self.__head:
            if self.__head.has_next():
                self.__head = self.__head.next()
            else: 
                self.__head = None
        self.__size -= 1