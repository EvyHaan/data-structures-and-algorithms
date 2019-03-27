from ..hashtable.hashtable import Hashtable
from ..linked_list.linked_list import LinkedList, Node
from .left_join import left_join


def test_tables_have_matches():
    ht1 = Hashtable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outfit', 'garb')
    ht1.add('guide', 'usher')

    ht2 = Hashtable()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')

    expected = [
        ['diligent', 'employed', 'idle'],
        ['outfit', 'garb', None],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['wrath', 'anger', 'delight']
        ]
    actual = left_join(ht1, ht2)
    assert actual == expected


def test_tables_no_matches():
    ht1 = Hashtable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outfit', 'garb')
    ht1.add('guide', 'usher')

    ht2 = Hashtable()
    ht2.add('inclined', 'averse')
    ht2.add('anger', 'delight')
    ht2.add('alert', 'idle')
    ht2.add('lead', 'follow')
    ht2.add('flow', 'jam')

    expected = [
        ['diligent', 'employed', None],
        ['outfit', 'garb', None],
        ['fond', 'enamored', None],
        ['guide', 'usher', None],
        ['wrath', 'anger', None]
        ]
    actual = left_join(ht1, ht2)
    assert actual == expected


def test_tables_empty_tables():
    ht1 = Hashtable()
    ht2 = Hashtable()

    expected = []
    actual = left_join(ht1, ht2)
    assert actual == expected


def test_right_table_is_empty():
    ht1 = Hashtable()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outfit', 'garb')
    ht1.add('guide', 'usher')

    ht2 = Hashtable()

    expected = [
        ['diligent', 'employed', None],
        ['outfit', 'garb', None],
        ['fond', 'enamored', None],
        ['guide', 'usher', None],
        ['wrath', 'anger', None]
        ]
    actual = left_join(ht1, ht2)
    assert actual == expected
