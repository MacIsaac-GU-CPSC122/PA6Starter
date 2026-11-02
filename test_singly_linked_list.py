# NOTE: do not modify the contents of this file
import pytest
from singly_linked_list import SinglyLinkedList, _Node, Empty


# NOTE: order is actual/received student value, expected/solution
def test_str():
    sll = SinglyLinkedList()
    assert str(sll) == "head->None"

    sll._head = _Node(10)
    assert str(sll) == "head->10->None"

    sll._head = _Node(20, _Node(10, _Node(30)))
    assert str(sll) == "head->20->10->30->None"

def test_len():
    sll = SinglyLinkedList()
    assert len(sll) == 0

    sll._head = _Node(10)
    assert len(sll) == 1

    sll._head = _Node(20, _Node(10, _Node(30)))
    assert len(sll) == 3

def test_is_empty():
    sll = SinglyLinkedList()
    assert sll.is_empty() is True

    sll._head = _Node(10)
    assert sll.is_empty() is False

def test_clear():
    sll = SinglyLinkedList()
    sll._head = _Node(10, _Node(20, _Node(30)))

    sll.clear()
    assert sll._head is None

def test_add_to_front():
    sll = SinglyLinkedList()

    sll.add_to_front(10)
    assert sll._head is not None
    assert sll._head._item == 10
    assert sll._head._next is None

    sll.add_to_front(20)
    assert sll._head._item == 20
    assert sll._head._next is not None
    assert sll._head._next._item == 10
    assert sll._head._next._next is None

    sll.add_to_front(30)
    assert sll._head._item == 30
    assert sll._head._next._item == 20
    assert sll._head._next._next._item == 10
    assert sll._head._next._next._next is None

def test_delete_at_front():
    sll = SinglyLinkedList()

    with pytest.raises(Empty):
        sll.delete_at_front()

    sll._head = _Node(30, _Node(20, _Node(10)))

    assert sll.delete_at_front() == 30
    assert sll._head._item == 20
    assert sll._head._next._item == 10
    assert sll._head._next._next is None

    assert sll.delete_at_front() == 20
    assert sll._head._item == 10
    assert sll._head._next is None

    assert sll.delete_at_front() == 10
    assert sll._head is None

    with pytest.raises(Empty):
        sll.delete_at_front()

def test_add_to_back():
    sll = SinglyLinkedList()

    # empty list case
    sll.add_to_back(10)
    assert sll._head is not None
    assert sll._head._item == 10
    assert sll._head._next is None

    # non-empty list case
    sll = SinglyLinkedList()
    sll._head = _Node(10, _Node(20))
    sll.add_to_back(30)

    assert sll._head._item == 10
    assert sll._head._next._item == 20
    assert sll._head._next._next._item == 30
    assert sll._head._next._next._next is None

def test_delete_at_back():
    sll = SinglyLinkedList()

    with pytest.raises(Empty):
        sll.delete_at_back()

    # one node list
    sll._head = _Node(10)
    assert sll.delete_at_back() == 10
    assert sll._head is None

    # multi node list
    sll._head = _Node(10, _Node(20, _Node(30)))

    assert sll.delete_at_back() == 30
    assert sll._head._item == 10
    assert sll._head._next._item == 20
    assert sll._head._next._next is None

    assert sll.delete_at_back() == 20
    assert sll._head._item == 10
    assert sll._head._next is None

    assert sll.delete_at_back() == 10
    assert sll._head is None

def test_delete():
    sll = SinglyLinkedList()

    # deleting from empty list should do nothing
    sll.delete(99)
    assert sll._head is None

    # delete middle node
    sll._head = _Node(10, _Node(20, _Node(30, _Node(40))))
    sll.delete(20)
    assert sll._head._item == 10
    assert sll._head._next._item == 30
    assert sll._head._next._next._item == 40
    assert sll._head._next._next._next is None

    # delete first node
    sll._head = _Node(10, _Node(20, _Node(30)))
    sll.delete(10)
    assert sll._head._item == 20
    assert sll._head._next._item == 30
    assert sll._head._next._next is None

    # delete last node
    sll._head = _Node(10, _Node(20, _Node(30)))
    sll.delete(30)
    assert sll._head._item == 10
    assert sll._head._next._item == 20
    assert sll._head._next._next is None

    # delete value not in list: no change
    sll._head = _Node(10, _Node(20, _Node(30)))
    sll.delete(999)
    assert sll._head._item == 10
    assert sll._head._next._item == 20
    assert sll._head._next._next._item == 30
    assert sll._head._next._next._next is None

def test_search():
    sll = SinglyLinkedList()
    assert sll.search(10) is False

    sll._head = _Node(10, _Node(20, _Node(30)))
    assert sll.search(10) is True
    assert sll.search(20) is True
    assert sll.search(30) is True
    assert sll.search(999) is False

def test_get_item_at_index():
    sll = SinglyLinkedList()
    assert sll.get_item_at_index(0) is None

    sll._head = _Node(10, _Node(20, _Node(30)))
    assert sll.get_item_at_index(0) == 10
    assert sll.get_item_at_index(1) == 20
    assert sll.get_item_at_index(2) == 30
    assert sll.get_item_at_index(3) is None
    assert sll.get_item_at_index(-1) is None

def test_reverse():
    sll = SinglyLinkedList()

    # empty list
    sll.reverse()
    assert sll._head is None

    # one node list
    sll._head = _Node(10)
    sll.reverse()
    assert sll._head._item == 10
    assert sll._head._next is None

    # multi node list
    sll._head = _Node(10, _Node(20, _Node(30, _Node(40))))
    sll.reverse()
    assert sll._head._item == 40
    assert sll._head._next._item == 30
    assert sll._head._next._next._item == 20
    assert sll._head._next._next._next._item == 10
    assert sll._head._next._next._next._next is None

# BONUS
def test_insert_in_order():
    sll = SinglyLinkedList()

    # empty list
    sll.insert_in_order(10)
    assert sll._head._item == 10
    assert sll._head._next is None

    # insert at front
    sll._head = _Node(10, _Node(20))
    sll.insert_in_order(5)
    assert sll._head._item == 5
    assert sll._head._next._item == 10
    assert sll._head._next._next._item == 20
    assert sll._head._next._next._next is None

    # insert in middle
    sll._head = _Node(5, _Node(10, _Node(20)))
    sll.insert_in_order(7)
    assert sll._head._item == 5
    assert sll._head._next._item == 7
    assert sll._head._next._next._item == 10
    assert sll._head._next._next._next._item == 20
    assert sll._head._next._next._next._next is None

    # insert at end
    sll._head = _Node(5, _Node(10, _Node(20)))
    sll.insert_in_order(30)
    assert sll._head._item == 5
    assert sll._head._next._item == 10
    assert sll._head._next._next._item == 20
    assert sll._head._next._next._next._item == 30
    assert sll._head._next._next._next._next is None

    # insert duplicate
    sll._head = _Node(5, _Node(10, _Node(20)))
    sll.insert_in_order(10)
    assert sll._head._item == 5
    assert sll._head._next._item == 10
    assert sll._head._next._next._item == 10
    assert sll._head._next._next._next._item == 20
    assert sll._head._next._next._next._next is None