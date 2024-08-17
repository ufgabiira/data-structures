class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next
    def __str__(self) -> str:
        return f"{self._data}"
    def next(self):
        return  self._next
    def set_next(self, node):
        self._next = node

class LinkedList:
    def __init__(self, head=None):
        self._head = head
    def head(self):
        return self._head
    def append(self, data) -> None:
        if self._head:
            current = self._head
            while current.next():
                current = current.next()
            current.set_next(Node(data))
        else:
            self._head = Node(data)
    def print_list(self):
        string = "["
        if self._head:
            current = self._head
            while current.next():
                string = f"{string}{current}, "
                current = current.next()
            string = f"{string}{current}]"
        else:
            string = "Empty list."
        return string

def count_nodes(linked_list) -> int:
    i = 0
    current = linked_list.head()
    while current.next():
        i += 1
        current = current.next()
    i += 1
    return i

l = LinkedList()
l.append("Gabriel")
l.append(24)
l.append(1.82)

print("list: ", l.print_list())
print("node count = ", count_nodes(l))