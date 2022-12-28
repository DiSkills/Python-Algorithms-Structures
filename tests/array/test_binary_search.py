from src.array.binary_search import binary_search


def test_binary_search_found_element_index() -> None:
    data = [1, 2, 3, 4, 9, 15, 44]
    index = binary_search(data=data, element=2)
    assert index == 1


def test_binary_search_found_one_of_the_indexes() -> None:
    data = [1, 1, 2, 2, 2, 3, 4, 15, 15, 70]
    index = binary_search(data=data, element=2)
    assert index in (2, 3, 4)


def test_binary_search_not_find_index_of_missing_element() -> None:
    data = [1, 2, 3, 4, 9, 15, 44]
    index = binary_search(data=data, element=150)
    assert index is None

    index = binary_search(data=data, element=-1)
    assert index is None
