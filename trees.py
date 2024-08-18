""" Tree implementation by Gabriel Ferreira (github.com/ufgabiira)
TODO: implement TreeNode and Tree classes __str__ method
TODO: finish documentation
"""

from typing import Self

class TreeNode:
    """ Represents a node in a the Tree object.

    Attributes
    ----------
    _data : any
        the content stored in the node
    _children : list[TreeNode]
        a list of the children nodes
    _parent : TreeNode
        the parent node

    Methods
    -------
    data
        returns the _data attribute
    children
        returns the _children attribute
    parent
        returns the _parent attribute
    set_data(new_data)
        set a new value for the note content (__data attribute)
    add_child(data)
        appends a new TreeNode object to the _children list
    remove_child(data)
        removes the child that has 'data' as its content
    """

    def __init__(self, data=None) -> None:
        self.__data = data
        self.__children = []
        self.__parent = None

    def data(self):
        return self.__data
    
    def children(self) -> list[Self]:
        return self.__children
    
    def parent(self) -> Self|None:
        return self.__parent
    
    def set_data(self, new_data):
        self.__data = new_data
        return self.__data
    
    def add_child(self, data) -> None:
        new_node = TreeNode(data)
        new_node.__parent = self
        self.__children.append(new_node)
        
    def remove_self(self) -> None:
        parent = self.parent()
        if parent:
            parent.__children.remove(self)


class Tree:
    def __init__(self) -> None:
        self.__root = TreeNode()

    def __get_node(self, node, data):
        if node.data() == data:
            return node
        for child in node.children():
            target = self.__get_node(child, data)
            if target is not None:
                return target
        
    def add_at(self, new_data, parent_data=None):
        target = self.__get_node(self.__root, parent_data)
        if target:
            target.add_child(new_data)

    def remove(self, node_data):
        target = self.__get_node(self.__root, node_data)
        if target is not None:
            target.remove_self()
        else:
            raise Exception(f"Object could not be found.")
        
    def find(self, value):
        return self.__get_node(self.__root, value)


if __name__ == "__main__":
    t = Tree()
    t.add_at("Notebook")
    t.add_at("Smartphone")    
    t.add_at("Tablet")

    t.add_at(parent_data="Smartphone", new_data="Redmi Note 13")
    t.add_at(parent_data="Smartphone", new_data="Poco X3 NFC")
    t.add_at("Samsung Galaxy Tab S6 Lite", "Tablet")

    print(t.find("Samsung Galaxy Tab S6 Lite"))

    t.remove("Notebook")
    t.remove("Tablet")
    t.remove("Redmi Note 13")
    
    print(t)