class Node():
    """The node class instantiates a new node."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree():
    """The BinaryTree class instantiates a new binary tree with traversal methods."""

    def __init__(self):
        self.root = None

    def preorder(self, current=None):
        """Function to return binary tree in preorder as an array"""

        pre_order_list = []

        if not self.root:
            return pre_order_list

        if not current:
            current = self.root

        pre_order_list.append(current.value)

        if current.left_child is not None:
            pre_order_list += self.preorder(current.left_child)

        if current.right_child is not None:
            pre_order_list += self.preorder(current.right_child)

        return pre_order_list

    def inorder(self, current=None):
        """Function to return binary tree in inorder as an array"""
        in_order_list = []

        if not self.root:
            return in_order_list

        if not current:
            current = self.root

        if current.left_child is not None:
            in_order_list += self.inorder(current.left_child)

        in_order_list.append(current.value)

        if current.right_child is not None:
            in_order_list += self.inorder(current.right_child)

        return in_order_list

    def postorder(self, current=None):
        """Function to return binary tree in postorder as an array"""
        post_order_list = []

        if not self.root:
            return post_order_list

        if not current:
            current = self.root

        if current.left_child is not None:
            post_order_list += self.postorder(current.left_child)

        if current.right_child is not None:
            post_order_list += self.postorder(current.right_child)

        post_order_list.append(current.value)

        return post_order_list


class BinarySearchTree(BinaryTree):
    """The BinarySearchTree class instantiates a new binary tree with methods to add and search for values."""

    def add(self, value):
        node = Node(value)
        self._add_node(node)

    def _add_node(self, node, current=None):
        """Function to add a node to a binary search tree"""
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
        """Function that returns a boolean if a value can be found in a binary tree"""
        current = self.root

        if self.root is None:
            return False

        while value != current.value:
            if value < current.value and current.left_child:
                current = current.left_child
            elif value > current.value and current.right_child:
                current = current.right_child
            else:
                return False

        return True

    def fizz_buzz_tree(self, current=None):

        current = self.root

        if current.left_child is not None:
            self.fizz_buzz_tree(current.left_child)

        if current.value % 3 == 0 and current.value % 5 == 0:
            current.value = 'FizzBuzz'
        if current.value % 3 == 0:
            current.value = 'Fizz'
        if current.value % 5 == 0:
            current.value = 'Buzz'

        if current.right_child is not None:
            self.fizz_buzz_tree(current.right_child)

        return in_order_list
