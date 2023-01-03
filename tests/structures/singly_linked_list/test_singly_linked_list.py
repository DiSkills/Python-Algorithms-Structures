from src.structures.singly_linked_list import Node, LinkedList


def test_list_repr() -> None:
    linked_list = LinkedList()
    assert linked_list.__repr__() == 'None'

    linked_list.push_back(1)
    assert linked_list.__repr__() == '1 -> None'

    linked_list.push_back(2)
    assert linked_list.__repr__() == '1 -> 2 -> None'


def test_list_iter() -> None:
    linked_list = LinkedList()
    assert list(linked_list) == []

    linked_list.push_back(1)
    assert list(linked_list) == [Node(data=1)]

    linked_list.push_back(2)
    assert list(linked_list) == [Node(data=1), Node(data=2)]


def test_list_push_back() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    # Append first
    linked_list.push_back(1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list.head is not None
    assert linked_list.head.data == 1

    assert linked_list.tail is not None
    assert linked_list.tail.data == 1

    # Append second
    linked_list.push_back(2)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '1 -> 2 -> None'

    assert linked_list.head.data == 1
    assert linked_list.tail.data == 2

    # Append left (zero)
    linked_list.append_left(0)
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '0 -> 1 -> 2 -> None'

    assert linked_list.head.data == 0
    assert linked_list.tail.data == 2


def test_list_append_left() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    # Append first
    linked_list.append_left(1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list.head is not None
    assert linked_list.head.data == 1

    assert linked_list.tail is not None
    assert linked_list.tail.data == 1

    # Append zero
    linked_list.append_left(0)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '0 -> 1 -> None'

    assert linked_list.head.data == 0
    assert linked_list.tail.data == 1

    # Append right (second)
    linked_list.push_back(2)
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '0 -> 1 -> 2 -> None'

    assert linked_list.head.data == 0
    assert linked_list.tail.data == 2


def test_create_list_with_empty_start_data() -> None:
    linked_list = LinkedList(data=[])
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    assert linked_list.head is None
    assert linked_list.tail is None


def test_create_list_with_many_start_data() -> None:
    linked_list = LinkedList(data=[1, 2, 3])
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '1 -> 2 -> 3 -> None'

    assert linked_list.head is not None
    assert linked_list.head.data == 1
    assert linked_list.tail is not None
    assert linked_list.tail.data == 3


def test_create_list_with_one_item_in_start_data() -> None:
    linked_list = LinkedList(data=[1])
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list.head is not None
    assert linked_list.head.data == 1
    assert linked_list.tail is not None
    assert linked_list.tail.data == 1
