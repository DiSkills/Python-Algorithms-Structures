import pytest

from src.structures.singly_linked_list import LinkedList


def test_iter() -> None:
    linked_list = LinkedList()
    assert list(linked_list) == []

    linked_list.push_back(1)
    assert [node.data for node in linked_list] == [1]

    linked_list.push_back(2)
    assert [node.data for node in linked_list] == [1, 2]


@pytest.mark.parametrize('index', range(-3, 3))
def test_get_item(index) -> None:
    data = [1, 2, 3]
    linked_list = LinkedList(data=data)
    assert linked_list[index] == data[index]


@pytest.mark.parametrize('index', range(-5, 5))
def test_get_node_in_empty_list(index) -> None:
    linked_list = LinkedList()

    with pytest.raises(IndexError, match='SinglyLinkedList is empty'):
        linked_list._get_node(index=index)


@pytest.mark.parametrize(
    'data, index',
    (
        ([1], -2),
        ([1], 1),
        ([1], 2),
        ([1, 2], -3),
        ([1, 2], 2),
        ([1, 2], 3),
    ),
)
def test_get_node_when_index_not_found(data, index) -> None:
    linked_list = LinkedList(data=data)

    with pytest.raises(
        IndexError, match=f'Node not found with index: {index}',
    ):
        linked_list._get_node(index=index)


@pytest.mark.parametrize('index', range(-5, 5))
def test_get_node(index) -> None:
    data = [1, 2, 3, 4, 5]
    linked_list = LinkedList(data=data)

    node = linked_list._get_node(index=index)
    assert node is not None
    assert node.data == data[index]
