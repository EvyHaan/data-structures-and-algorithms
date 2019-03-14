class Tode():
    """"""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return 'Tode with value: {}'.format(self.value)


class Quode():
    """The node class instantiates a new node.
    """

    def __init__(self, value):
        self.value = value
        self._next = None

    def __repr__(self):
        return 'Quode with value: {}'.format(self.value)


class Queue:

    front = None
    rear = None

    def enqueue(self, value):
        """
        """
        node = Quode(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            current = self.front
            while current._next:
                current = current._next

            current._next = node
            self.rear = current._next

    def dequeue(self):
        """
        """

        if not self.front:
            return 'Queue is empty'
        else:
            temp = self.front
            self.front = temp._next
            temp._next = None

        return temp.value

    def peek(self):

        front = self.front

        return front

    def __repr__(self):
        lst = []
        temp_q = self
        while temp_q.front:
            lst.append(temp_q.dequeue())
        return 'Queue: {}'.format(lst[::-1])


class Stack:

    top = None

    def peek(self):
        """
        """
        top = self.top

        return top

    def push(self, value):
        """
        """
        node = Quode(value)

        if not self.top:
            self.top = node
        else:
            current = self.top
            node._next = current
            self.top = node

    def pop(self):
        """
        """
        top = self.top

        if not top:
            return "The stack is empty"
        else:
            temp = top
            top = top._next
            temp._next = None

        return temp.value

    def pop_all(self):
        """
        """
        top = self.top

        if not top:
            return "The stack is empty"
        else:
            while top:
                temp = top
                top = top._next
                temp._next = None
        
        return temp.value


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
        node = Tode(value)
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