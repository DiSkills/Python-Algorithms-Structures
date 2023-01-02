from src.structures.singly_linked_list import Node


def test_node_repr() -> None:
    node = Node(data=1)
    assert node.__repr__() == '1'


def test_node_eq() -> None:
    node = Node(data=1)
    assert (node == 1) is False
    assert (node == Node(data=2)) is False
    assert (node == Node(data=1)) is True
