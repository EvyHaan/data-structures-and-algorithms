from .hashtable import Hashtable


def test_hash_string_key():
    ht = Hashtable()
    assert ht.hash('dd') == (200 * 599) % 1024


def test_hash_string_key_c():
    ht = Hashtable()
    assert ht.hash('cc') == (198 * 599) % 1024


def test_hash_not_string_key():
    ht = Hashtable()
    assert ht.hash(9) == (57 * 599) % 1024


def test_add_one():
    ht = Hashtable()
    ht.add('dd', 'dog')
    assert ht.table[1016].head.value == ('dd', 'dog')


def test_add_two_collision():
    ht = Hashtable()
    ht.add('dd', 'dog')
    ht.add('ag', 'gold')
    assert ht.table[1016].head.value == ('ag', 'gold')
    assert ht.table[1016].head._next.value == ('dd', 'dog')


def test_add_two_no_collision():
    ht = Hashtable()
    ht.add('dd', 'dog')
    ht.add('cc', 'cat')
    assert ht.table[1016].head.value == ('dd', 'dog')
    assert ht.table[842].head.value == ('cc', 'cat')


def test_contains_key_exists_as_bucket_head():
    ht = Hashtable()
    ht.add('dd', 'dog')
    assert ht.contains('dd') == True


def test_contains_key_exits_deep_in_bucket():
    ht = Hashtable()
    ht.add('dd', 'dog')
    ht.add('ag', 'gold')
    ht.add('ec', 'gdo')
    assert ht.contains('dd') == True


# WHY DOES THIS TEST *NOT* WORK IF I *DON'T* INCLUDE AN INIT WITH SELF.TABLE ?!?!?!?!
def test_contains_key_does_not_exist():
    ht = Hashtable()
    ht.add('ag', 'gold')
    ht.add('ec', 'gdo')
    assert ht.contains('dd') == False


def test_contains_key_empty_hashtable():
    ht = Hashtable()
    assert ht.contains('dd') == False


def test_get_key_exists_and_nested():
    ht = Hashtable()
    ht.add('dd', 'dog')
    ht.add('ag', 'gold')
    ht.add('ec', 'gdo')
    assert ht.get('ag') == 'gold'


def test_get_key_exists():
    ht = Hashtable()
    ht.add('dd', 'dog')
    assert ht.get('dd') == 'dog'


def test_get_key_does_not_exist():
    ht = Hashtable()
    ht.add('cc', 'cat')
    assert ht.get('ag') == None


def test_get_empty_hashtable():
    ht = Hashtable()
    assert ht.get('cc') == None
