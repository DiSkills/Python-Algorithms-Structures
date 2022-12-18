def _sum(*, numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 0
    return numbers.pop(-1) + _sum(numbers=numbers)


def main() -> None:
    print(_sum(numbers=[]))
    print(_sum(numbers=[4]))
    print(_sum(numbers=[2, 4, 6]))


if __name__ == '__main__':
    main()
