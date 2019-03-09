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

    def preorder(self, current=None):

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

