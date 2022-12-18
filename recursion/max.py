def _max(*, numbers: list[int]) -> int | None:
    if len(numbers) == 0:
        return None

    element = numbers.pop(-1)
    maximum = _max(numbers=numbers)
    if maximum is None:
        return element
    if element > maximum:
        return element
    return maximum


def main() -> None:
    print(_max(numbers=[]))
    print(_max(numbers=[5]))
    print(_max(numbers=[1, 5, 10, 6, 8]))
    print(_max(numbers=[1, 101, 5, 10, 99, 100, 10, 100, 101, 101, 6, 8]))


if __name__ == '__main__':
    main()
