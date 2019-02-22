from linked_list import LinkedList


def test_exists():
    assert LinkedList


def test_instantiation():
    """Can successfully instantiate an empty linked list
    """
    assert LinkedList()


def test_insert():
    """Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual


def test_insert_two():
    """Can properly insert multiple nodes into the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples')
    fruits.insert('bananas')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual

    expected = 'bananas'
    actual = fruits.head._next.value

    assert expected == actual


def test_includes():
    """Will return true when finding a value within the linked list that exists
    Will return false when searching for a value in the linked list that does not exist
    """
    fruits = LinkedList()
    fruits.insert('apples')
    fruits.insert('bananas')
    fruits.insert('dates')

    assert fruits.includes('bananas')


def test_not_includes():
    fruits = LinkedList()
    fruits.insert('apples')
    fruits.insert('bananas')
    fruits.insert('dates')

    assert not fruits.includes('zucchini')


def test_print():
    """Can properly return a collection of all the values that exist in the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples')
    fruits.insert('bananas')
    fruits.insert('dates')

    assert fruits.print() == 'apples,bananas,dates,'


# def test of empty string
def test_print():
    """Can return an empty string if the linked list is empty
    """
    fruits = LinkedList()

    assert fruits.print() == ''
