from src.structures.singly_linked_list import Node


def test_node_repr_and_str() -> None:
    node = Node(data=1)
    assert node.__repr__() == '1'
    assert node.__str__() == '1'
