from tree import Node, BinaryTree, BinarySearchTree

# ====== Binary Search Tree tests ======

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


def test_search_one_node_truthy():
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
    bst = BinarySearchTree()

    expected = False
    actual = bst._contains(10)

    assert actual == expected

# ====== Binary Tree Tests =======


def test_BTree_class_exists():
    assert BinaryTree


def test_BTree_instantiation():
    assert BinaryTree()


def test_preorder():
    tree = BinarySearchTree()
    tree.add('D')
    tree.add('B')
    tree.add('A')
    tree.add('C')
    tree.add('F')
    tree.add('E')

    assert tree.preorder() == ['D', 'B', 'A', 'C', 'F', 'E']


def test_preorder():
    tree = BinarySearchTree()

    assert tree.preorder() == []


def test_inorder():
    tree = BinarySearchTree()

    assert tree.inorder() == []


def test_inorder():
    tree = BinarySearchTree()
    tree.add('D')
    tree.add('B')
    tree.add('A')
    tree.add('C')
    tree.add('F')
    tree.add('E')

    assert tree.inorder() == ['A', 'B', 'C', 'D', 'E', 'F']


def test_postorder():
    tree = BinarySearchTree()

    assert tree.postorder() == []


def test_postorder():
    tree = BinarySearchTree()
    tree.add('D')
    tree.add('B')
    tree.add('A')
    tree.add('C')
    tree.add('F')
    tree.add('E')

    assert tree.postorder() == ['A', 'C', 'B', 'E', 'F', 'D']
