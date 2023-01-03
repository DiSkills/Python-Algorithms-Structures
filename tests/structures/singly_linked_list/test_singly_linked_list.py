import pytest

from src.structures.singly_linked_list import LinkedList


def test_repr() -> None:
    linked_list = LinkedList()
    assert linked_list.__repr__() == 'None'

    linked_list.push_back(1)
    assert linked_list.__repr__() == '1 -> None'

    linked_list.push_back(2)
    assert linked_list.__repr__() == '1 -> 2 -> None'


def test_iter() -> None:
    linked_list = LinkedList()
    assert list(linked_list) == []

    linked_list.push_back(1)
    assert [node.data for node in linked_list] == [1]

    linked_list.push_back(2)
    assert [node.data for node in linked_list] == [1, 2]


def test_push_back() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    # Push first
    linked_list.push_back(1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1

    # Push second
    linked_list.push_back(2)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '1 -> 2 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 1
    assert linked_list.tail == 2

    # Push front (zero)
    linked_list.push_front(0)
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '0 -> 1 -> 2 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 0
    assert linked_list.tail == 2


def test_push_front() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    # Push first
    linked_list.push_front(1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1

    # Push zero
    linked_list.push_front(0)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '0 -> 1 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 0
    assert linked_list.tail == 1

    # Push back (second)
    linked_list.push_back(2)
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '0 -> 1 -> 2 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 0
    assert linked_list.tail == 2


def test_create_with_empty_start_data() -> None:
    linked_list = LinkedList(data=[])
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None


def test_create_with_many_start_data() -> None:
    linked_list = LinkedList(data=[1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '1 -> 2 -> 3 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 1
    assert linked_list.tail == 3


def test_create_with_one_item_in_start_data() -> None:
    linked_list = LinkedList(data=[1])
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1


def test_pop_front_in_empty_list() -> None:
    linked_list = LinkedList(data=[])
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None

    with pytest.raises(IndexError, match='SinglyLinkedList is empty'):
        linked_list.pop_front()

    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None


def test_pop_front_when_head_equal_tail() -> None:
    linked_list = LinkedList(data=[1])
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1

    linked_list.pop_front()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None


def test_pop_front_when_length_equal_2() -> None:
    linked_list = LinkedList(data=[1, 2])
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '1 -> 2 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 1
    assert linked_list.tail == 2

    linked_list.pop_front()
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '2 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 2


def test_pop_front() -> None:
    linked_list = LinkedList(data=[1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '1 -> 2 -> 3 -> None'

    assert linked_list.head == 1
    assert linked_list.tail == 3

    linked_list.pop_front()
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '2 -> 3 -> None'

    assert linked_list.head == 2
    assert linked_list.tail == 3
