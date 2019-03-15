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


class Hashtable:
    def __init__(self):
        self.table = [None] * 1024

    def hash(self, key):
        stringified_key = str(key)
        ascii_sum = 0
        for c in stringified_key:
            ascii_sum += ord(c)
        bucket_number = (ascii_sum * 599) % 1024
        return bucket_number

    def add(self, key, value):
        idx = self.hash(key)

        if not self.table[idx]:
            # bucket = LinkedList()
            self.table[idx] = LinkedList()

        self.table[idx].ll_insert((key, value))
        print(self.table[idx].head.value)

    def get(self, key):
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
