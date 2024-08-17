class Node:
    def __init__(self, data) -> None:
        self.__data = data
        self.__children = []

    def data(self):
        return self.__data
    
    def children(self):
        return self.__children
    
    def set_data(self, new_data):
        self.__data = new_data
        return self.__data
    
    def append_child(self, child):
        if child is Node:
            self.__children.append(child)
            return True
        else:
            return False
        
    def remove_child(self, index=None, data=None):
        if index and index is int:
            return self.__children.pop(index)
        elif data:
            return self.__children.remove(data)
        else:
            return False
        
class Tree:
    def __init__(self) -> None:
        self.__root = None

    def add_at(self, parent_data, new_child_data):
        current = self.__root
        if current:
            pass
