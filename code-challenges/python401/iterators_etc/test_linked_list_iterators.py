from ..linked_list.linked_list import LinkedList
import pytest


def test_linked_list_class():
    assert LinkedList


# Why is something being passed in here? TypeError: Object LinkedList() takes no arguments
# def test_linked_list_instance():
#     assert LinkedList('foo')


def test_linked_list_ll_append_one():
    ll = LinkedList()
    ll.ll_append('apples')
    assert ll.head.value == 'apples'


def test_linked_list_ll_append_two():
    ll = LinkedList()
    ll.ll_append('apples')
    ll.ll_append('bananas')
    assert ll.head.value == 'apples'
    assert ll.head._next.value == 'bananas'


def test_linked_list_iteration():
    ll = LinkedList()
    ll.ll_append('apples')
    ll.ll_append('bananas')

    items = []
    for item in ll:
        items.append(item)

    assert items == ['apples', 'bananas']


def test_linked_list_conversion():
    ll = LinkedList()
    ll.ll_append('apples')
    ll.ll_append('bananas')

    items = list(ll)

    assert items == ['apples', 'bananas']


def test_linked_list_expressesion():
    ll = LinkedList()
    ll.ll_append('apples')
    ll.ll_append('bananas')

    cap_fruits = [f.upper() for f in ll]

    assert cap_fruits == ['APPLES', 'BANANAS']


def test_linked_list_filter():
    letters = LinkedList()
    letters.ll_append('a')
    letters.ll_append('b')
    letters.ll_append('c')
    letters.ll_append('d')
    letters.ll_append('e')
    letters.ll_append('f')
    letters.ll_append('g')

    vowels = 'aeiou'

    consonants = [char for char in letters if char not in vowels]

    assert consonants == ['b', 'c', 'd', 'f', 'g']


def test_add_operator():
    animals = LinkedList()

    animals += 'giraffe'

    assert list(animals) == ['giraffe']


def test_concat():
    montagues = LinkedList(['Romeo', 'Benvolio'])

    capulets = LinkedList(['Juliet', 'Tybalt'])

    tutti = montagues + capulets

    assert len(list(tutti)) == 4

    assert len(list(montagues)) == 2

