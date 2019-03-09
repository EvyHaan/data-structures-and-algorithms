from tree import Node, BinaryTree, BinarySearchTree


def test_BST_class_exists():
    assert BinarySearchTree


def test_BST_instantiation():
    assert BinarySearchTree()


def test_add_one_node():
    bst = BinarySearchTree()
    bst.add(6)

    assert bst.root.value == 6


def test_add_two_nodes():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)

    assert bst.root.value == 10
    assert bst.root.left_child.value == 5


def test_add_three_nodes():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(20)

    assert bst.root.value == 10
    assert bst.root.left_child.value == 5
    assert bst.root.right_child.value == 20


def test_add_five_nodes():
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


def test_add_five_nodes():
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


def test_add_five_nodes():
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
