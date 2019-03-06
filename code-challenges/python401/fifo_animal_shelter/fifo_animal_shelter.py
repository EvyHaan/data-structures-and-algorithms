class Node():
    """The node class instantiates a new node.
    """
    def __init__(self, value):
        self.value = value
        self._next = None


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        """
        node = Node(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            current = self.front
            while current._next:
                current = current._next

            current._next = node
            self.rear = current._next

    def dequeue(self):
        """
        """
        if not self.front:
            return None
        else:
            temp = self.front
            self.front = temp._next
            temp._next = None

        return temp.value


class Animal_Shelter():
    def __init__(self):
        self.Hold1 = Queue()
        self.Hold2 = Queue()

    def enqueue(self, animal):
        self.Hold1.enqueue(animal)

    def dequeue(self, pref):
        while pref == 'cat' or pref == 'dog':

            if self.Hold2.front:
                if self.Hold2.front == pref:
                    return self.Hold2.dequeue()
            
            if self.Hold1.front:
                while self.Hold1.front != pref:
                    pet = self.Hold1.dequeue()
                    self.Hold2.enqueue(pet)
                return self.Hold1.dequeue()
            
            return None

        return None
