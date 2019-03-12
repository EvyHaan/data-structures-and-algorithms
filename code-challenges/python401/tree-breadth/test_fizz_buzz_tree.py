from breadth_first import breadth_first
from support_items import Queue
from fizz_buzz_tree import BinarySearchTree


def test_class_exists():
    assert BinarySearchTree


def test_fizzbuzztree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(15)
    tree.add(11)
    tree.fizz_buzz_tree()

    print(breadth_first(tree))
    assert tree.root.value == 'Fizz'

    # ['Fizz', 'Buzz', 7, 'Buzz', 11, 'FizzBuzz']
