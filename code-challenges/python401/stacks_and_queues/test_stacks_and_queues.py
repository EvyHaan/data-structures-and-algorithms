from stacks_and_queues import Stack, Queue

#  ===============Stack Tests===============


def test_stack_exits():
    """Test to verify the class of "Stack" exits.
    """
    assert Stack


def test_stack_instantiation():
    """Can successfully instantiate an empty stack.
    """
    assert Stack()


def test_stack_peek():
    """Can successfully peek the next item on the stack.
    """
    laundry = Stack()
    laundry.push('socks')
    laundry.push('jeans')

    assert laundry.top.value == 'jeans'


def test_empty_stack_peek():
    """Can successfully peek at an empty stack.
    """
    laundry = Stack()

    assert not laundry.top


def test_push():
    """Can successfully push a node on a stack.
    """
    laundry = Stack()
    laundry.push('socks')

    expected = 'socks'
    actual = laundry.top.value

    assert expected == actual


def test_push():
    """Can successfully push multiple nodes on a stack.
    """
    laundry = Stack()
    laundry.push('socks')
    laundry.push('jeans')
    laundry.push('shirt')

    expected = 'shirt'
    actual = laundry.top.value

    assert expected == actual


def test_empty_stack_pop():
    """Can successfully notify if a stack is empty before popping.
    """
    laundry = Stack()

    expected = 'The stack is empty'
    actual = laundry.pop()

    assert expected == actual


def test_one_pop():
    """Can successfully pop an item off a stack.
    """
    laundry = Stack()
    laundry.push('socks')
    laundry.push('jeans')
    laundry.push('shirt')

    expected = 'shirt'
    actual = laundry.pop()

    assert expected == actual


def test_two_pop():
    """Can successfully pop all items off a stack.
    """
    laundry = Stack()
    laundry.push('socks')
    laundry.push('jeans')
    laundry.push('shirt')

    expected = 'socks'
    actual = laundry.pop_all()

    assert expected == actual

# ==================Queue Tests============


def test_queue_exits():
    """Test to verify the class of "Queue" exits.
    """
    assert Queue


def test_queue_instantiation():
    """Can successfully instantiate an empty queue.
    """
    assert Queue()


def test_enqueue_one():
    line = Queue()
    line.enqueue('Pam')

    assert line.rear.value == 'Pam'


def test_enqueue_two():
    """Can successfully enqueue items.
    """
    line = Queue()
    line.enqueue('Pam')
    line.enqueue('Jim')

    assert line.rear.value == 'Jim'



def test_one_dequeue():
    """Can successfully dequeue an item.
    """
    line = Queue()
    line.enqueue('Pam')
    line.enqueue('Jim')
    line.enqueue('Dwight')

    expected = 'Pam'
    actual = line.dequeue()

    assert expected == actual