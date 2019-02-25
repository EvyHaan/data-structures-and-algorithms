"""This module defines defines operations for a singly linked lists.
"""


class LinkedList:
    """A class that instantiates a new linked lists
    """

    head = None

    # WRITE NEW FUNCTION FOR INSERT AT BEGINNING
    def ll_insert(self, value):
        """Function to insert a new node into a singly linked list
        """
        node = Node(value)

        if value == '':
            return('Node needs a value')

        if not self.head:
            self.head = node
        else:
            current = self.head

            while current._next:
                current = current._next

            current._next = node

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

        return(result)
    
    def ll_append(self, value):
        """Function to insert a new node into a singly linked list
        """
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current = self.head

            while current._next:
                current = current._next

            current._next = node
    
    def ll_insert_before(self, value, new_value):

        node = Node(new_value)

        if not self.head:
            self.head = node
        else:
            current = self.head

        while current._next:
            if current._next.value == value:
                node._next = current._next
                current._next = node
                break
            else:
                current = current._next
        
    def ll_insert_after(self, value, new_value):

        node = Node(new_value)

        if not self.head:
            self.head = node
        else:
            current = self.head
        
        while current._next:
            if current._next.value == value:
                node._next = current._next._next
                current = current._next
                current._next = node
                break
            else:
                current = current._next


class Node():
    """The node class instantiates a new node.
    """
    def __init__(self, value):
        self.value = value
        self._next = None
