class LinkedList:
    """A class that instantiates a new linked lists
    """

    head = None

    def ll_insert(self, value):
        """Function to insert a new node into a singly linked list
        """
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head

            while current._next:
                current = current._next

            current._next = Node(value)

    def ll_includes(self, value):
        """Function to search for a value in a linked list
        """
        current = self.head

        while current:
            if current.value == value:
                return True

            current = current._next

        return False

    def ll_print(self):
        """Function to print the values of the linked list
        """
        result = ''
        current = self.head

        while current:
            result += '- ' + current.value + ' -'
            current = current._next

        return result


class Node():
    """The node class instantiates a new node.
    """
    def __init__(self, value):
        self.value = value
        self._next = None
