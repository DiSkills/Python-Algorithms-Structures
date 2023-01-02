from src.structures.singly_linked_list import Node, LinkedList


def test_node_repr() -> None:
    node = Node(data=1)
    assert node.__repr__() == '1'


def test_list_append() -> None:
    linked_list = LinkedList()
    assert len(linked_list) == 0

    linked_list.append(1)
    assert len(linked_list) == 1

    assert linked_list.head is not None
    assert linked_list.head.data == 1

    assert linked_list.tail is not None
    assert linked_list.tail.data == 1

    linked_list.append(2)
    assert len(linked_list) == 2

    assert linked_list.head is not None
    assert linked_list.head.data == 1

    assert linked_list.tail is not None
    assert linked_list.tail.data == 2


def test_list_repr() -> None:
    linked_list = LinkedList()
    assert linked_list.__repr__() == 'None'

    linked_list.append(1)
    assert linked_list.__repr__() == '1 -> None'

    linked_list.append(2)
    assert linked_list.__repr__() == '1 -> 2 -> None'
