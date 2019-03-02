from stacks_and_queues import Stack


def test_stack_exits():
    """
    """
    assert Stack


def test_add_to_top():
    fruits = Stack._list
    fruits.ll_insert('apples')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual


def test_two_to_top():
    fruits = Stack._list
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')

    expected = 'bananas'
    actual = fruits.head.value

    assert expected == actual
