from src.array.binary_search_boundaries import get_boundaries


def test_get_boundaries_of_an_existing_element() -> None:
    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    assert get_boundaries(data=data, target=3) == (2, 5)

    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    assert get_boundaries(data=data, target=1) == (0, 0)

    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    assert get_boundaries(data=data, target=5) == (7, 7)

    data = [5, 7, 7, 8, 8, 10]
    assert get_boundaries(data=data, target=8) == (3, 4)

    data = [2, 2]
    assert get_boundaries(data=data, target=2) == (0, 1)

    data = [2]
    assert get_boundaries(data=data, target=2) == (0, 0)


def test_get_boundaries_in_empty_list() -> None:
    data: list[int] = []
    assert get_boundaries(data=data, target=3) == (-1, -1)


def test_get_boundaries_of_non_existing_element() -> None:
    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    assert get_boundaries(data=data, target=10) == (-1, -1)

    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    assert get_boundaries(data=data, target=-1) == (-1, -1)

    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    assert get_boundaries(data=data, target=6) == (-1, -1)

    data = [2, 2]
    assert get_boundaries(data=data, target=3) == (-1, -1)
