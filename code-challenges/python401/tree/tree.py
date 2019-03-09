class Node():
    """The node class instantiates a new node.
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def preorder(self, root):
        pass

    def inorder(self, root):
        pass

    def postorder(self, root):
        pass


class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = Node(value)
        self._add_node(node)

    def _add_node(self, node, current=None):
        if self.root is None:
            self.root = node

        if current is None:
            current = self.root

        if current:
            if current.value > node.value:
                if current.left_child is None:
                    current.left_child = node
                else:
                    self._add_node(node, current.left_child)

            if current.value < node.value:
                if current.right_child is None:
                    current.right_child = node
                else:
                    self._add_node(node, current.right_child)

    def _contains(self, value):

        if self.root is None:
            return False
        else:
            current = self.root

        while current.left_child is not None and current.right_child is not None:
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:
                return True
        return False
        
