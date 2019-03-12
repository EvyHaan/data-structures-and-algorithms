from support_items import BinarySearchTree, Queue


def breadth_first(tree):
    breadth_queue = Queue()
    lst = []

    breadth_queue.enqueue(tree.root)

    while breadth_queue.peek():
        current = breadth_queue.dequeue()

        if current.left_child:
            breadth_queue.enqueue(current.left_child)

        if current.right_child:
            breadth_queue.enqueue(current.right_child)

        lst.append(current.value)
    
    return lst
