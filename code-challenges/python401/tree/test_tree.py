from tree import Node, BinaryTree, BinarySearchTree
from support_items import Queue, Stack

# ====== Binary Search Tree tests ======


def test_BST_class_exists():
    """Tests that a BinarySearchTree class exists"""
    assert BinarySearchTree


def test_BST_instantiation():
    """Tests that a binary search tree is instantiated"""
    assert BinarySearchTree()


def test_add_one_node():
    """Can add a node to a binary search tree"""
    bst = BinarySearchTree()
    bst.add(6)

    assert bst.root.value == 6


def test_add_two_nodes():
    """Can add multiple nodes/levels to a binary search tree"""
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)

    assert bst.root.value == 10
    assert bst.root.left_child.value == 5


def test_add_three_nodes():
    """Can add multiple nodes/levels to a binary search tree"""
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(20)

    assert bst.root.value == 10
    assert bst.root.left_child.value == 5
    assert bst.root.right_child.value == 20


def test_add_five_nodes():
    """Can add multiple nodes/levels to a binary search tree"""
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(20)
    bst.add(8)
    bst.add(15)

    assert bst.root.value == 10
    assert bst.root.left_child.value == 5
    assert bst.root.right_child.value == 20
    assert bst.root.left_child.right_child.value == 8
    assert bst.root.right_child.left_child.value == 15


def test_search_one_node_truthy():
    """Can successfully find a value that exists in a binary search tree"""
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(20)
    bst.add(8)
    bst.add(15)

    expected = True
    actual = bst._contains(8)

    assert actual == expected


def test_search_another_node_truthy():
    """Can successfully find a value that exists in a binary search tree"""
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(20)
    bst.add(8)
    bst.add(15)

    expected = True
    actual = bst._contains(5)

    assert actual == expected


def test_search_falsey():
    """Can successfully determine that a value does not exist in a binary search tree"""
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(20)
    bst.add(8)
    bst.add(15)

    expected = False
    actual = bst._contains(25)

    assert actual == expected


def test_search_falsey():
    """Can successfully determin that no values exist in an empty binary search tree"""
    bst = BinarySearchTree()

    expected = False
    actual = bst._contains(10)

    assert actual == expected

# ====== Binary Tree Tests =======


def test_BTree_class_exists():
    """Tests that a BinarySearchTree class exists"""
    assert BinaryTree


def test_BTree_instantiation():
    """Tests that a binary search tree is instantiated"""
    assert BinaryTree()


def test_preorder():
    """Successfully returns an array of preordered values from a binary tree"""
    tree = BinarySearchTree()
    tree.add('D')
    tree.add('B')
    tree.add('A')
    tree.add('C')
    tree.add('F')
    tree.add('E')

    assert tree.preorder() == ['D', 'B', 'A', 'C', 'F', 'E']


def test_preorder():
    """Successfully returns an empty array from an empty binary tree"""
    tree = BinarySearchTree()

    assert tree.preorder() == []


def test_inorder():
    """Successfully returns an array of inordered values from a binary tree"""
    tree = BinarySearchTree()

    assert tree.inorder() == []


def test_inorder():
    """Successfully returns an empty array from an empty binary tree"""
    tree = BinarySearchTree()
    tree.add('D')
    tree.add('B')
    tree.add('A')
    tree.add('C')
    tree.add('F')
    tree.add('E')

    assert tree.inorder() == ['A', 'B', 'C', 'D', 'E', 'F']


def test_postorder():
    """Successfully returns an empty array from an empty binary tree"""
    tree = BinarySearchTree()

    assert tree.postorder() == []


def test_postorder():
    """Successfully returns an array of postordered values from a binary tree"""
    tree = BinarySearchTree()
    tree.add('D')
    tree.add('B')
    tree.add('A')
    tree.add('C')
    tree.add('F')
    tree.add('E')

    assert tree.postorder() == ['A', 'C', 'B', 'E', 'F', 'D']


def test_breadth_traversal():
    tree = BinarySearchTree()
    queue = Queue()
    tree.add(5)
    tree.add(4)
    tree.add(10)
    tree.add(2)

    assert tree.breadth_first(tree) == [5, 4, 10, 2]
    assert tree.breadth_first(tree) != [5, 4, 10, 3]


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

    assert tree.root.value == 'Buzz'

    # Should Be: ['Fizz', 'Buzz', 7, 'Buzz', 11, 'FizzBuzz']


def test_find_max_value():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(15)
    tree.add(11)

    assert tree.find_max_value() == 15
