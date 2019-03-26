from ..hashtable.hashtable import Hashtable, Node
from ..tree.tree import BinarySearchTree, BinaryTree, Node


def tree_intersection(tree1, tree2):
    shared_values = []
    tree_table = Hashtable()

    def hash_tree(tree):

        tree_table.add(tree.value, tree_table.hash(tree.value))

        if tree.left_child:
            hash_tree(tree.left_child)

        if tree.right_child:
            hash_tree(tree.right_child)

        return tree_table

    def compare(table, tree):
        if table.contains(tree.value):
            shared_values.append(tree.value)

        if tree.left_child:
            compare(table, tree.left_child)

        if tree.right_child:
            compare(table, tree.right_child)

    if tree1 and tree2:
        compare(hash_tree(tree1), tree2)

    if len(shared_values) > 0:
        return shared_values
    else:
        return None
