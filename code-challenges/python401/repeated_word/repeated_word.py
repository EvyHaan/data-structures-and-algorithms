from ..hashtable.hashtable import Hashtable, Node
import re


def repeated_word(sentance):
    rgx = r"\W+"
    words = sentance.split(' ')
    ht = Hashtable()

    for word in words:
        word = re.sub(rgx, '', word).lower()
        if ht.contains(word):
            return word
        else:
            ht.add(word, None)
