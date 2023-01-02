def get_left_boundary(*, data: list[int], target: int) -> int:
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if target == data[middle]:
            high = middle - 1
        elif target < data[middle]:
            high = middle - 1
        else:
            low = middle + 1
    if (0 <= low < len(data)) and (data[low] == target):
        return low
    return -1


def get_right_boundary(*, data: list[int], target: int) -> int:
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if target == data[middle]:
            low = middle + 1
        elif target < data[middle]:
            high = middle - 1
        else:
            low = middle + 1
    if (0 <= high < len(data)) and (data[high] == target):
        return high
    return -1


def get_boundaries(*, data: list[int], target: int) -> tuple[int, int]:
    left_boundary = get_left_boundary(data=data, target=target)
    right_boundary = get_right_boundary(data=data, target=target)
    return left_boundary, right_boundary


def main() -> None:
    data = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    print(get_boundaries(data=data, target=3))


if __name__ == '__main__':
    main()
