from .support_items import Queue, Stack
import math


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

    def traverse_in_order(self):
        """Traverse a tree in in-order using a generator."""

        def _traverse(current):
            if not current:
                return
            yield from _traverse(current.left_child)
            yield current.value
            yield from _traverse(current.right_child)

        return _traverse(self.root)

    def traverse_pre_order(self):
        """Traverse a tree in pre-order using a generator."""

        def _traverse(current):
            if not current:
                return
            yield current.value
            yield from _traverse(current.left_child)
            yield from _traverse(current.right_child)
        return _traverse(self.root)

    def traverse_post_order(self):
        """Traverse a tree in post-order using a generator."""

        def _traverse(current):
            if not current:
                return
            yield from _traverse(current.left_child)
            yield from _traverse(current.right_child)
            yield current.value
        return _traverse(self.root)

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

    def breadth_first(self, current=None):
        breadth_queue = Queue()
        lst = []

        if not current:
            current = self.root

        breadth_queue.enqueue(self.root)

        while breadth_queue.peek():
            current = breadth_queue.dequeue()

            if current.left_child:
                breadth_queue.enqueue(current.left_child)

            if current.right_child:
                breadth_queue.enqueue(current.right_child)

            lst.append(current.value)

        return lst

    def traverse_breadth_first(self):
        """Traverse a tree breadth-first using a generator."""
        def _traverse(current):

            if not current:
                return

            breadth_queue = Queue()
            breadth_queue.enqueue(current)

            while breadth_queue.peek():
                current = breadth_queue.dequeue()
                yield current.value
                if current.left_child:
                    breadth_queue.enqueue(current.left_child)
                if current.right_child:
                    breadth_queue.enqueue(current.right_child)
            yield from _traverse(current.left_child)
            yield from _traverse(current.right_child)

        return _traverse(self.root)

    def pre_order_max(self, current=None, max_so_far=None):

        if not self.root:
            return None

        if not current:
            current = self.root
            max_so_far = current.value

        max_so_far = max(current.value, max_so_far)

        if current.left_child is not None:
            max_from_child = self.pre_order_max(current.left_child, max_so_far)
            max_so_far = max(max_from_child, max_so_far)

        if current.right_child is not None:
            max_from_child = self.pre_order_max(
                current.right_child, max_so_far)
            max_so_far = max(max_from_child, max_so_far)

        return max_so_far

    def find_max_value(self):
        return self.pre_order_max()


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

        if not current:
            current = self.root

        if current.left_child:
            self.fizz_buzz_tree(current.left_child)

        if isinstance(current.value, int):
            if current.value % 3 == 0 and current.value % 5 == 0:
                current.value = 'FizzBuzz'
            elif current.value % 3 == 0:
                current.value = 'Fizz'
            elif current.value % 5 == 0:
                current.value = 'Buzz'

        if current.right_child:
            self.fizz_buzz_tree(current.right_child)

        return self
