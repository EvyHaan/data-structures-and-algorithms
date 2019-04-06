from ..tree.tree import BinarySearchTree
import pytest


def test_class():
    assert BinarySearchTree


def test_traverse_in():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_in_order())

    assert items == ['apples', 'bananas', 'cucumbers']


def test_traverse_pre():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_pre_order())

    assert items == ['bananas', 'apples', 'cucumbers']


def test_traverse_post():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_post_order())

    assert items == ['apples', 'cucumbers', 'bananas']


def test_traverse_breadth():
    tree = BinarySearchTree()
    tree.add('dates')
    tree.add('figs')
    tree.add('cucumbers')
    tree.add('apples')
    tree.add('bananas')
    tree.add('elderberries')

    items = list(tree.traverse_breadth_first())

    assert items == ['dates', 'cucumbers', 'figs', 'apples', 'bananas', 'elderberries']


def test_traverse_for_loop():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_in_order():
        items.append(item)

    assert items == ['apples', 'bananas', 'cucumbers']


###### Recursive Yield Example ###
def traverse_in_order(self):

        def _traverse(node):
            if not node:
                return
            yield from _traverse(node.left)
            yield node.value
            yield from _traverse(node.right)

        return _traverse(self.root)
