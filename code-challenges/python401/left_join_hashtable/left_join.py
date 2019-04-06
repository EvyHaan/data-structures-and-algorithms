from ..hashtable.hashtable import Hashtable
from ..linked_list.linked_list import LinkedList, Node


def left_join(hashtable1, hashtable2):
    """Left joins two hash tables.

    Keys in the second provided table will be searched for matches to keys in the first, and their values will be added.

    Args:
        hashtable1 (hashtable): All keys and values from this table will be returned.
        hashtable2 (hashtable): Values whose keys match those in hashtable1 will be added to it's values.

    Returns:
        list: a matrix including the key, and any related values from.
    """
    lst = []
    for i in range(0, len(hashtable1.table)):
        if hashtable1.table[i]:
            current = hashtable1.table[i].head
            while current:
                search_key = current.value
                lst.append([search_key[0], search_key[1], hashtable2.get(search_key[0])])
                current = current._next
    return lst
