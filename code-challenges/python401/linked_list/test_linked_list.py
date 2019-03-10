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

    expected = 'bananas'
    actual = fruits.head.value

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

    assert fruits.ll_print() == '- dates -- bananas -- apples -'


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
    """Can return append a new node to the end of a linked list
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual


def test_append_two():
    """Can append two nodes to the end of a linked list
    """
    fruits = LinkedList()
    fruits.ll_append('apples')
    fruits.ll_append('bananas')

    expected = 'apples'
    actual = fruits.head.value

    assert expected == actual

    expected = 'bananas'
    actual = fruits.head._next.value

    assert expected == actual



def test_insert_before():
    """Can insert a new node before a given value
    """
    fruits = LinkedList()
    fruits.ll_append('apples')
    fruits.ll_append('bananas')
    fruits.ll_append('pears')

    fruits.ll_insert_before('pears', 'figs')

    assert fruits.ll_print() == '- apples -- bananas -- figs -- pears -'


def test_insert_after():
    """Can insert a node after a given value
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')
    fruits.ll_insert_after('bananas', 'figs')


def test_k_from_end():
    """Can return the value of a node at the kth position from the end of a linked list
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')
    fruits.ll_insert('figs')
    fruits.ll_insert('oranges')
    k = 2

    expected = 'pears'
    actual = fruits.ll_k_from_end(k)

    assert expected == actual


def test_k_empty_ll():
    """Will return a message if the linked list is empty
    """
    fruits = LinkedList()
    k = 3

    expected = 'empty linked list'
    actual = fruits.ll_k_from_end(k)

    assert expected == actual


def test_k_larger_than_ll():
    """Will return a message if the give kth position is larger than the length of the linked list
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')
    fruits.ll_insert('figs')
    fruits.ll_insert('oranges')

    assert fruits.ll_k_from_end(6) == 'Exception'


def test_ll_merge_same_length():
    """
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')
    fruits.ll_insert('figs')
    fruits.ll_insert('oranges')

    vegetables = LinkedList()
    vegetables.ll_insert('cucumers')
    vegetables.ll_insert('tomatos')
    vegetables.ll_insert('olives')
    vegetables.ll_insert('potatos')
    vegetables.ll_insert('cabbages')

    expected = fruits.head
    actual = fruits.ll_merge(vegetables)

    assert expected == actual


def test_ll_merge_both_empty_lists():
    """
    """
    fruits = LinkedList()
    vegetables = LinkedList()

    expected = 'empty linked list'
    actual = fruits.ll_merge(vegetables)

    assert expected == actual


def test_ll_merge_different_lengths():
    """
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')

    vegetables = LinkedList()
    vegetables.ll_insert('cucumers')
    vegetables.ll_insert('tomatos')

    expected = fruits.head
    actual = fruits.ll_merge(vegetables)

    assert expected == actual


def test_ll_merge_one_empty():
    """
    """
    fruits = LinkedList()
    fruits.ll_insert('apples')
    fruits.ll_insert('bananas')
    fruits.ll_insert('pears')

    vegetables = LinkedList()

    expected = fruits.head
    actual = fruits.ll_merge(vegetables)

    assert expected == actual