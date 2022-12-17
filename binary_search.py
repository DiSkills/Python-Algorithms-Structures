def binary_search(*, data: list[int], element: int) -> None | int:
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = data[middle]

        if guess == element:
            return middle

        if guess > element:
            high = middle - 1
        else:
            low = middle + 1

    return None


def main() -> None:
    data = [1, 3, 5, 7, 9]
    print(binary_search(data=data, element=3))
    print(binary_search(data=data, element=-1))


if __name__ == '__main__':
    main()
