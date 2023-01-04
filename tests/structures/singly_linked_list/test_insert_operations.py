import pytest

from src.structures.singly_linked_list import LinkedList


@pytest.mark.parametrize(
    'function', (LinkedList.push_front, LinkedList.push_back),
)
def test_push_in_empty_list(function) -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    function(linked_list, 1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1


@pytest.mark.parametrize(
    'function, expected_repr, expected_head, expected_tail',
    (
        (LinkedList.push_front, '2 -> 1 -> None', 2, 1),
        (LinkedList.push_back, '1 -> 2 -> None', 1, 2),
    ),
)
def test_push(function, expected_repr, expected_head, expected_tail) -> None:
    linked_list = LinkedList(data=[1])
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1

    function(linked_list, 2)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == expected_repr

    assert linked_list._head != linked_list._tail
    assert linked_list.head == expected_head
    assert linked_list.tail == expected_tail
