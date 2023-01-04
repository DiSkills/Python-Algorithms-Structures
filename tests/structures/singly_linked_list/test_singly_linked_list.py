from src.structures.singly_linked_list import LinkedList


def test_repr() -> None:
    linked_list = LinkedList()
    assert linked_list.__repr__() == 'None'

    linked_list.push_back(1)
    assert linked_list.__repr__() == '1 -> None'

    linked_list.push_back(2)
    assert linked_list.__repr__() == '1 -> 2 -> None'


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
