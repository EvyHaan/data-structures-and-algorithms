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
            node._next = current
            self.head = node

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
        """Function to insert a new node into a singly linked list before a given value
        """
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
        """Function to insert a new node into a singly linked list after a given value
        """
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

    def ll_k_from_end(self, k):
        """Function to find a value of a node at the kth position from the end.
        """
        total_nodes = 0
        position = 0
        current = self.head

        while current and current._next:
            total_nodes += 1
            current = current._next

        if current and not current._next:
            total_nodes += 1
        else:
            return 'empty linked list'

        if k < total_nodes:
            position = total_nodes - k
        else:
            return 'Exception'

        current = self.head

        for i in range(1, position):
            current = current._next

        return current.value

    def ll_merge(self, list2):
        head1 = self.head
        head2 = self.head

        if not head1 and not head2:
            return 'empty linked list'
        
        if head1 and not head2:
            return head1
        
        if not head1 and head2:
            return head2
        
        if head1 and head2:
            curr1 = head1
            curr2 = head2

            while curr1._next is not None and curr2._next is not None:
                ref1 = curr1._next
                ref2 = curr2._next

                curr1._next = curr2
                curr2._next = ref1

                curr1 = ref1
                curr2 = ref2

            if curr1._next is None and curr2:
                curr1._next = curr2
                return head1
            if curr2._next is None and curr1:
                ref1 = curr1._next
                curr1.next = curr2
                curr2.next = ref1
                return head1










    #     if not self.head:
    #         if list2.head:
    #             head1 = list2.head
    #         else:
    #             head1 = None
    #     else:
    #         head1 = self.head
    #         if list2.head:
    #             head2 = list2.head
    #         else:
    #             head2 = list2.head

    #     if head1 and head2:
    #         curr1 = head1
    #         curr2 = head2
    #         ref1 = head1
    #         ref2 = head2

    #         while curr1._next or curr2._next:
    #             ref1 = curr1._next
    #             ref2 = curr2._next
    #             curr2._next = ref1
    #             curr1._next = curr2
    #             curr2 = ref2
    #             curr1 = ref1
    #             # if not curr1._next or not curr2._next:
    #             #     break

    #         if curr1._next:
    #             curr2._next = ref1
    #         else:
    #             curr1._next = ref2

    #     else:
    #         head1 = None

    #     return head1


class Node():
    """The node class instantiates a new node.
    """

    def __init__(self, value):
        self.value = value
        self._next = None
