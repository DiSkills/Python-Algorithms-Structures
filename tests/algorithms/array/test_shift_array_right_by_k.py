from src.algorithms.array.shift_array_right_by_k import shift_array


def test_shift_the_array_to_the_right_by_less_than_its_length() -> None:
    data = [1, 2, 3, 4, 5, 6, 7]
    data = shift_array(array=data)
    assert data == [7, 1, 2, 3, 4, 5, 6]

    data = [1, 2, 3, 4, 5, 6, 7]
    data = shift_array(array=data, k=3)
    assert data == [5, 6, 7, 1, 2, 3, 4]


def test_shift_the_array_to_the_right_by_its_length() -> None:
    data = [1, 2, 3, 4, 5, 6, 7]
    data = shift_array(array=data, k=len(data))
    assert data == [1, 2, 3, 4, 5, 6, 7]


def test_shift_the_array_to_the_right_more_than_its_length() -> None:
    data = [1, 2, 3, 4, 5, 6, 7]
    data = shift_array(array=data, k=len(data) + 1)
    assert data == [7, 1, 2, 3, 4, 5, 6]

    data = [1, 2, 3, 4, 5, 6, 7]
    data = shift_array(array=data, k=len(data) + 3)
    assert data == [5, 6, 7, 1, 2, 3, 4]
