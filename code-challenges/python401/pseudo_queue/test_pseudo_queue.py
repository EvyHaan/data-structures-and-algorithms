from pseudo_queue import Pseudo_Queue


def test_class_exits():
    assert Pseudo_Queue


def test_class_instantiation():
    assert Pseudo_Queue()


def test_enqueue_one_empty_stack():
    queue = Pseudo_Queue()
    queue.enqueue('sheep')

    assert queue._in_stack.peek().value == 'sheep'


def test_enqueue_three_full_stack():
    queue = Pseudo_Queue()
    queue.enqueue('sheep')
    queue.enqueue('pig')
    queue.enqueue('rooster')

    assert queue._in_stack.peek().value == 'rooster'


def test_dequeue_empty_stacks():
    queue = Pseudo_Queue()

    expected = 'no items in pseudo queue'
    actual = queue.dequeue()

    assert actual == expected


def test_dequeue_empty_second_stack():
    queue = Pseudo_Queue()
    queue.enqueue('sheep')
    queue.enqueue('pig')
    queue.enqueue('rooster')
    queue.dequeue()

    assert queue._out_stack.peek().value == 'pig'


def test_dequeue_stacks_full():
    queue = Pseudo_Queue()
    queue.enqueue('sheep')
    queue.enqueue('pig')
    queue.enqueue('rooster')
    queue.dequeue()
    queue.enqueue('bunny')
    queue.enqueue('goat')
    queue.enqueue('cow')
    queue.dequeue()

    assert queue._out_stack.peek().value == 'rooster'