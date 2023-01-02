def choice_sort(*, data: list[int]) -> list[int]:
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]
    return data


def main() -> None:
    data = [5, 3, 6, 2, 10]
    print(choice_sort(data=data))


if __name__ == '__main__':
    main()
