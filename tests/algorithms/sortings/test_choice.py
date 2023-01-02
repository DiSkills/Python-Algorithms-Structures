import random

from src.algorithms.sortings.choice import choice_sort


def test_sorting_random_list() -> None:
    data = list(range(-100, 100))
    random.shuffle(data)
    assert choice_sort(data=data[:]) == sorted(data)


def test_sorting_sorted_list() -> None:
    data = list(range(-100, 100))
    assert choice_sort(data=data[:]) == data


def test_sorting_inverted_list() -> None:
    data = list(range(100, -100, -1))
    assert choice_sort(data=data[:]) == sorted(data)
