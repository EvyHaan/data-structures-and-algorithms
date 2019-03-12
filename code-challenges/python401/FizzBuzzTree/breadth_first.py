# import binary tree


def breadth_first(tree):
    breadth_queue = Queue()

    breadth_queue.enqueue(tree.root):

    while queue.peek():
        current = breadth_queue.dequeue()

        if current.left_child:
            breadth_queue.enqueue()

        if current.right_child:
            breadth_queue.dequeue()

        print(current.value)
