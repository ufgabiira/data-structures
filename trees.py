""" Tree implementation by Gabriel Ferreira (github.com/ufgabiira)
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
        self.__depth = 0

    def __str__(self) -> str:
        return f"{self.__data}"

    def data(self):
        return self.__data
    
    def children(self) -> list[Self]:
        return self.__children
    
    def parent(self) -> Self|None:
        return self.__parent

    def depth(self):
        return self.__depth

    def subtree(self):
        string = ""
        if self.__data:
            string = f"{(self.__depth-1)*'  |__'}{self.__data}\n"
        for child in self.children():
            string = f"{string}{child.subtree()}"
        else:
            return string
    
    def set_data(self, new_data):
        self.__data = new_data
        return self.__data
    
    def add_child(self, data, depth) -> None:
        new_node = TreeNode(data)
        new_node.__parent = self
        new_node.__depth = depth
        self.__children.append(new_node)
        
    def remove_self(self) -> None:
        parent = self.parent()
        if parent:
            parent.__children.remove(self)


class Tree:
    def __init__(self) -> None:
        self.__root = TreeNode()
        self.__height = 0
        self.__count = 0

    def __str__(self) -> str:
        return self.__root.subtree()

    def __get_node(self, node, data):
        self.__count += 1
        if node.data() == data:
            return node
        for child in node.children():
            target = self.__get_node(child, data)
            if target is not None:
                return target
            self.__count -= 1
        
    def add_at(self, new_data, parent_data=None):
        self.__count = 0
        target = self.__get_node(self.__root, parent_data)
        if target:
            if self.__count > self.__height:
                self.__height = self.__count
            target.add_child(new_data, self.__count)

    def remove(self, node_data):
        target = self.__get_node(self.__root, node_data)
        if target is not None:
            target.remove_self()
        else:
            raise Exception(f"Object could not be found.")
        
    def find(self, value):
        return self.__get_node(self.__root, value)
