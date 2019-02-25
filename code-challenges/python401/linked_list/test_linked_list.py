from linked_list import LinkedList


def test_exists():
    """The class exists
    """
    assert LinkedList


def test_instantiation():
    """Can successfully instantiate an empty linked list
    """
    assert LinkedList()

# WRITE NEW TESTS FOR INSERT AT BEGINNING
def test_insert():
    """Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual


def test_insert_two():
    """Can properly insert multiple nodes into the linked list
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual

    expected = 'bananas'
    actual = fruits.head._next.value

    assert expected == actual


def test_includes():
    """Will return true when finding a value within the linked list that exists
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('dates')

    assert fruits.ll_includes('bananas')


def test_not_includes():
    """Will return false when searching for a value in the linked list that does not exist
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('dates')

    assert not fruits.ll_includes('zucchini')


def test_print():
    """Can properly return a collection of all the values that exist in the linked list
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('dates')

    assert fruits.ll_print() == '- apples -- bananas -- dates -'


def test_print_empty_ll():
    """Can return an empty string if the linked list is empty
    """
    fruits = LinkedList()

    assert fruits.ll_print() == ''


def test_no_value():
    """Will return a message if a value is not provided.
    """
    fruits = LinkedList()

    assert fruits.ll_insert('') == 'Node needs a value'


def test_append():
    fruits = LinkedList()
    fruits.ll_insert('apples')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual


def test_append_two():
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual

    expected = 'bananas'
    actual = fruits.head._next.value

    assert expected == actual


def test_insert_before():
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')

    fruits.ll_insert_before('pears', 'figs')

    assert fruits.ll_print() == '- apples -- bananas -- figs -- pears -'


def test_insert_after():
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')
    fruits.ll_insert_after('bananas', 'figs')

    assert fruits.ll_print() == '- apples -- bananas -- figs -- pears -'