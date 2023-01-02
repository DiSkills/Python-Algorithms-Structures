from src.algorithms.recursion.factorial import factorial


def test_get_factorial() -> None:
    assert factorial(number=6) == 1 * 2 * 3 * 4 * 5 * 6

    assert factorial(number=10) == 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
