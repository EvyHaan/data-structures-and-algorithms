from fifo_animal_shelter import Animal_Shelter, Queue


def test_class_exits():
    assert Animal_Shelter


def test_class_instantiation():
    assert Animal_Shelter()


def test_enqueue_one_empty_hold1():
    shelter = Animal_Shelter()
    shelter.enqueue('dog')

    assert shelter.Hold1.front.value == 'dog'


def test_enqueue_three_full_hold1_front():
    shelter = Animal_Shelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')

    assert shelter.Hold1.front.value == 'dog'


def test_enqueue_three_full_hold1_rear():
    shelter = Animal_Shelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')

    assert shelter.Hold1.rear.value == 'cat'


def test_dequeue_empty_shelter():
    shelter = Animal_Shelter()

    expected = None
    actual = shelter.dequeue('cat')

    assert actual == expected

# ::::


# def test_dequeue_empty_hold1_first_matches():
#     shelter = Animal_Shelter()
#     shelter.enqueue('dog')
#     shelter.enqueue('dog')
#     shelter.dequeue('dog')

#     assert shelter.Hold1.front.value == 'dog'


# def test_dequeue_two_different_spaced_pets():
#     shelter = Animal_Shelter()
#     shelter.enqueue('dog')
#     shelter.enqueue('dog')
#     shelter.enqueue('cat')
#     shelter.dequeue('cat')
#     shelter.enqueue('dog')
#     shelter.enqueue('cat')
#     shelter.enqueue('cat')
#     shelter.dequeue('dog')

#     assert shelter.Hold1.front.value == 'cat'
