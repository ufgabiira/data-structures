class TreeNode:
    def __init__(self, key=None, depth=0, parent=None):
        self.__key = key
        self.__depth = depth
        self.__parent = parent
        self.__left = None
        self.__right = None

    def __str__(self):
        return f"{self.__key}"

    # getters
    def key(self):
        return self.__key
    
    def depth(self):
        return self.__depth

    def parent(self):
        return self.__parent
    
    def left(self):
        return self.__left
    
    def right(self):
        return self.__right
    
    # setters
    def set_key(self, value):
        self.__key = value
    
    def set_parent(self, node):
        self.__parent = node
    
    def set_left(self, node):
        self.__left = node
    
    def set_right(self, node):
        self.__right = node
    

class BinaryTree():
    def __init__(self):
        self.__root = TreeNode(depth=0)
        self.__height = 0

    # returns the tree formated as a set, sorted in crescent order
    def __str__(self):
        string = "{"
        def aux(node, string):
            left = node.left()
            right = node.right()
            if left:
                string = aux(left, string)
            if node.key():
                string = f"{string}{node}, "
            if right:
                string = aux(right, string)
            return string
        string = aux(self.__root, string)[:-2] + "}"
        return string 

    # returns the tree formated as a set, sorted in crescent order
    def in_order_set(self):
        string = "{"
        def aux(node, string):
            left = node.left()
            right = node.right()
            if left:
                string = aux(left, string)
            if node.key():
                string = f"{string}{node}, "
            if right:
                string = aux(right, string)
            return string
        string = aux(self.__root, string)[:-2] + "}"
        return string 
    
    # inserts a new node
    def insert(self, key):
        def add_to(node):
            if key > node.key():
                if not node.right():
                    new_node = TreeNode(key=key, depth=node.depth()+1, parent=node)
                    node.set_right(new_node)
                    if node.depth()+1 > self.__height:
                        self.__height = node.depth()+1
                else: 
                    add_to(node.right())
            elif key < node.key():
                if not node.left():
                    new_node = TreeNode(key=key, depth=node.depth()+1, parent=node)
                    node.set_left(new_node)
                    if node.depth()+1 > self.__height:
                        self.__height = node.depth()+1
                else:
                    add_to(node.left())
        if not self.__root.key():
            self.__root.set_key(key)
        else:
            add_to(self.__root)

    # 'get' method auxiliary function
    def __get(self, node, key):
            if node and node.key():
                if key == node.key():
                    return node
                if key < node.key():
                    return self.__get(node.left(), key)
                else:
                    return self.__get(node.right(), key)

    # returns the searched node object
    def get(self, key):
        return self.__get(self.__root, key)

    # gets the node with smallest key
    def __smallest_node(self, node):
        if node.left():
            return self.__smallest_node(node.left())
        return node
        
    # removes a node object
    def remove(self, key):
        node = self.get(key)
        if node and node.parent():
            # removes a leaf
            if not node.left() and not node.right():
                if node == node.parent().left(): 
                    node.parent().set_left(None)
                else: 
                    node.parent().set_right(None)

            # removes a node with only the left child
            elif node.left() and not node.right():
                if node == node.parent().left(): 
                    node.parent().set_left(node.left())
                else: 
                    node.parent().set_right(node.left())
            
            # removes a node with only the right child
            elif not node.left() and node.right():
                if node == node.parent().left(): 
                    node.parent().set_left(node.right())
                else: 
                    node.parent().set_right(node.right())

            # removes a node with both children
            else:
                smallest = self.__smallest_node(node.right())
                temp = smallest.key()
                smallest.set_key(node.key())
                node.set_key(temp)
                if smallest.right():
                    smallest.parent().set_left(smallest.right())
                else:
                    smallest.parent().set_left(None)