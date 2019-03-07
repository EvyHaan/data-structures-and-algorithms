class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        """
        """
        top = self.top

        if not top:
            return None
        else:
            return top.value

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
            return None
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


class BracketValidation():
    def __init__(self):
        self.brack_stack = Stack()

    def bracket_validation(self, phrase):
        """
        """
        for char in phrase:
            if char == '(' or char == '{' or char == '[':
                self.brack_stack.push(char)

            if char == ')':
                if self.brack_stack.peek() == '(':
                    self.brack_stack.pop()
                else:
                    return False

            if char == '}':
                if self.brack_stack.peek() == '{':
                    self.brack_stack.pop()
                else:
                    return False

            if char == ']':
                if self.brack_stack.peek() == '[':
                    self.brack_stack.pop()
                else:
                    return False
        
        if self.brack_stack.peek():
            return False
        else:
            return True
