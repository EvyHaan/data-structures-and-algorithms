from ..hashtable.hashtable import Hashtable, Node
from ..tree.tree import BinarySearchTree, Node
from .tree_intersection import tree_intersection


def test_intersections_exist():
    tree1 = BinarySearchTree()
    tree1.add('D')
    tree1.add('B')
    tree1.add('A')
    tree1.add('C')
    tree1.add('F')
    tree1.add('E')

    tree2 = BinarySearchTree()
    tree2.add('H')
    tree2.add('E')
    tree2.add('A')
    tree2.add('G')
    tree2.add('J')
    tree2.add('K')

    expected = ['E', 'A']
    actual = tree_intersection(tree1.root, tree2.root)
    assert expected == actual


def test_intersections_do_not_exist():
    tree1 = BinarySearchTree()
    tree1.add('D')
    tree1.add('B')
    tree1.add('A')
    tree1.add('C')
    tree1.add('F')
    tree1.add('E')

    tree2 = BinarySearchTree()
    tree2.add('H')
    tree2.add('EE')
    tree2.add('AA')
    tree2.add('G')
    tree2.add('J')
    tree2.add('K')

    expected = None
    actual = tree_intersection(tree1.root, tree2.root)
    assert expected == actual


def test_both_empty_trees():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    expected = None
    actual = tree_intersection(tree1.root, tree2.root)
    assert expected == actual
