import pytest

from src.structures.singly_linked_list import LinkedList


@pytest.mark.parametrize(
    'function', (LinkedList.pop_front, LinkedList.pop_back),
)
def test_pop_in_empty_list(function) -> None:
    linked_list = LinkedList(data=[])
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None

    with pytest.raises(IndexError, match='SinglyLinkedList is empty'):
        function(linked_list)

    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None


@pytest.mark.parametrize(
    'function', (LinkedList.pop_front, LinkedList.pop_back),
)
def test_pop_when_head_equal_tail(function) -> None:
    linked_list = LinkedList(data=[1])
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list._head == linked_list._tail
    assert linked_list.head == 1

    function(linked_list)
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None


@pytest.mark.parametrize(
    'function, expected_repr, expected_head',
    (
        (LinkedList.pop_front, '2 -> None', 2),
        (LinkedList.pop_back, '1 -> None', 1),
    ),
)
def test_pop_when_length_equal_2(
    function, expected_repr, expected_head,
) -> None:
    linked_list = LinkedList(data=[1, 2])
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '1 -> 2 -> None'

    assert linked_list._head != linked_list._tail
    assert linked_list.head == 1
    assert linked_list.tail == 2

    function(linked_list)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == expected_repr

    assert linked_list._head == linked_list._tail
    assert linked_list.head == expected_head


@pytest.mark.parametrize(
    'function, expected_repr, expected_head, expected_tail',
    (
        (LinkedList.pop_front, '2 -> 3 -> None', 2, 3),
        (LinkedList.pop_back, '1 -> 2 -> None', 1, 2),
    ),
)
def test_pop(
    function, expected_repr, expected_head, expected_tail,
) -> None:
    linked_list = LinkedList(data=[1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '1 -> 2 -> 3 -> None'

    assert linked_list.head == 1
    assert linked_list.tail == 3

    function(linked_list)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == expected_repr

    assert linked_list.head == expected_head
    assert linked_list.tail == expected_tail
