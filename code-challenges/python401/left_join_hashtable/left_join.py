from ..hashtable.hashtable import Hashtable
from ..linked_list.linked_list import LinkedList, Node


def left_join(hashtable1, hashtable2):
    lst = []
    for i in range(0, len(hashtable1.table)):
        if hashtable1.table[i]:
            current = hashtable1.table[i].head
            while current:
                search_key = current.value
                if hashtable2.contains(search_key[0]):
                    lst.append([search_key[0], search_key[1], hashtable2.get(search_key[0])])
                else:
                    lst.append([search_key[0], search_key[1], None])
                current = current._next
    return lst
