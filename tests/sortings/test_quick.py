import random

from src.sortings.quick import quick_sort


def test_sorting_random_list() -> None:
    data = list(range(-100, 100))
    random.shuffle(data)
    assert quick_sort(data=data[:]) == sorted(data)


def test_sorting_sorted_list() -> None:
    data = list(range(-100, 100))
    assert quick_sort(data=data[:]) == data


def test_sorting_inverted_list() -> None:
    data = list(range(100, -100, -1))
    assert quick_sort(data=data[:]) == sorted(data)
