from hashtable import Hashtable


def test_hash_string_key():
    ht = Hashtable()
    assert ht.hash('dd') == (200 * 599) % 1024


def test_hash_not_string_key():
    ht = Hashtable()
    assert ht.hash(9) == (57 * 599) % 1024


def 