class Node():
    """The node class instantiates a new node.
    """

    def __init__(self, value):
        self.value = value
        self._next = None


class LinkedList:
    """A class that instantiates a new linked lists
    """

    head = None

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


class Hashtable:
    """Creates a Hashtable class."""

    def __init__(self):
        """Instantiates a hashtable with a table attribute."""
        self.table = [None] * 1024

    def hash(self, key):
        """Hashes a key to determine an index for storage.

        Parameters:
        key : any type
            A key to be used in a key-value pair. All inputs are stringified.
        """
        stringified_key = str(key)
        ascii_sum = 0
        for c in stringified_key:
            ascii_sum += ord(c)
        bucket_number = (ascii_sum * 599) % 1024
        return bucket_number

    def add(self, key, value):
        """Stores a key-value pair in the hashtable.

        Parameters:
        key : any type
            A key to be used in a key-value pair.
        value : any type
            A key's value.
        """
        idx = self.hash(key)

        if not self.table[idx]:
            self.table[idx] = LinkedList()

        self.table[idx].ll_insert((key, value))

    def get(self, key):
        """Retreives a value whos key matches the input.

        Parameters:
        key : any type
            The key of a key-value pair to be searched for.
        """
        idx = self.hash(key)

        if not self.table[idx]:
            return None

        current = self.table[idx].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current._next
        return None

    def contains(self, key):
        """Searches for the given key in the hashtable and returns a boolean.

        Parameters:
        key : any type
            The key of a key-value pair to be searched for.
        """
        idx = self.hash(key)

        if not self.table[idx]:
            return False

        current = self.table[idx].head
        while current:
            if current.value[0] == key:
                return True
            current = current._next
        return False

    def __repr__(self):
        pass


if __name__ == "__main__":
    ht = Hashtable()
    ht.add('ag', 'god')
    ht.add('ec', 'gdo')
    print(ht.contains('dd'))
    
