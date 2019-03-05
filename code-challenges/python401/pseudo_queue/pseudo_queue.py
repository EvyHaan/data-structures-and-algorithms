class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        """
        """
        top = self.top

        return top

    def push(self, value):
        """
        """
        node = Node(value)

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
            self.top = top._next
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


class Node():
    """The node class instantiates a new node.
    """

    def __init__(self, value):
        self.value = value
        self._next = None


class Pseudo_Queue:

    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()

    def enqueue(self, value):
        """
        """
        self._in_stack.push(value)

    def dequeue(self):
        """
        """
        if self._out_stack.top:
            return self._out_stack.pop()
        else:
            if self._in_stack.top:
                while self._in_stack.top:
                    value = self._in_stack.pop()
                    print(value)
                    self._out_stack.push(value)
                return self._out_stack.pop()
            else:
                return 'no items in pseudo queue'

