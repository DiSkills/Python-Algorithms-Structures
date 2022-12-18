def get_count_elements(*, data: list[int]) -> int:
    if len(data) == 0:
        return 0
    return 1 + get_count_elements(data=data[:-1])


def main() -> None:
    print(get_count_elements(data=[]))
    print(get_count_elements(data=[1]))
    print(get_count_elements(data=[1, 2, 3]))


if __name__ == '__main__':
    main()
