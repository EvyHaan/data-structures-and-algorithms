class Stack:

    top = None

    def peek():
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


class Pseudo_Queue:
    _in_stack = Stack()
    _out_stack = Stack()
