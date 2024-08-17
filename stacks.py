class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.previous = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.__size = 0

    def __str__(self) -> str:
        string = ""
        counter = 1
        pointer = self.top
        while pointer:
            string = f"{string}{counter}>{pointer.data}\n"
            counter += 1
            pointer = pointer.previous
            if not pointer: 
                break
        return string
    
    def size(self):
        return self.__size
    
    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.previous = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.__size += 1

    def pop(self):
        if self.top:
            if self.top.previous:
                self.top = self.top.previous
            else:
                self.top = None
