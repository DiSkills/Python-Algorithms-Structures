from src.structures.singly_linked_list import Node, LinkedList


def test_node_repr() -> None:
    node = Node(data=1)
    assert node.__repr__() == '1'


def test_node_eq() -> None:
    node = Node(data=1)
    assert (node == 1) is False
    assert (node == Node(data=2)) is False
    assert (node == Node(data=1)) is True


def test_list_append() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0

    linked_list.append(1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list.head is not None
    assert linked_list.head.data == 1

    assert linked_list.tail is not None
    assert linked_list.tail.data == 1

    linked_list.append(2)
    assert len(linked_list) == 2
    assert linked_list.__repr__() == '1 -> 2 -> None'

    assert linked_list.head.data == 1
    assert linked_list.tail.data == 2

    # Append left
    linked_list.append_left(0)
    assert len(linked_list) == 3
    assert linked_list.__repr__() == '0 -> 1 -> 2 -> None'

    assert linked_list.head.data == 0
    assert linked_list.tail.data == 2


def test_list_append_left() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert linked_list.__repr__() == 'None'

    linked_list.append_left(1)
    assert len(linked_list) == 1
    assert linked_list.__repr__() == '1 -> None'

    assert linked_list.head is not None
    assert linked_list.head.data == 1

    assert linked_list.tail is not None
    assert linked_list.tail.data == 1

    linked_list.append_left(0)
    assert len(linked_list) == 2

    assert linked_list.__repr__() == '0 -> 1 -> None'
    assert linked_list.head.data == 0
    assert linked_list.tail.data == 1

    # Append right
    linked_list.append(2)
    assert len(linked_list) == 3

    assert linked_list.__repr__() == '0 -> 1 -> 2 -> None'
    assert linked_list.head.data == 0
    assert linked_list.tail.data == 2


def test_list_repr() -> None:
    linked_list = LinkedList()
    assert linked_list.__repr__() == 'None'

    linked_list.append(1)
    assert linked_list.__repr__() == '1 -> None'

    linked_list.append(2)
    assert linked_list.__repr__() == '1 -> 2 -> None'


def test_list_iter() -> None:
    linked_list = LinkedList()
    assert list(linked_list) == []

    linked_list.append(1)
    assert list(linked_list) == [Node(data=1)]

    linked_list.append(2)
    assert list(linked_list) == [Node(data=1), Node(data=2)]
