def quick_sort(*, data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = []
    middle = []
    right = []
    for item in data:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            middle.append(item)
        else:
            right.append(item)
    return quick_sort(data=left) + middle + quick_sort(data=right)


def main() -> None:
    print(quick_sort(data=[10, 5, 2, 3]))
    print(quick_sort(data=[100, 50, 25, 3]))
    print(quick_sort(data=[2, 8, 5, 6, 54, 89, 5]))


if __name__ == '__main__':
    main()
