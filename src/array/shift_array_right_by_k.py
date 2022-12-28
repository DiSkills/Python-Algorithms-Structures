def reverse_array(
    *, array: list[int], right: int, left: int = 0,
) -> list[int]:
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array


def shift_array(*, array: list[int], k: int = 1) -> list[int]:
    k %= len(array)
    actions = (
        (0, len(array) - k - 1),
        (len(array) - k, len(array) - 1),
        (0, len(array) - 1),
    )
    for left, right in actions:
        array = reverse_array(array=array, left=left, right=right)
    return array


def main() -> None:
    array = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    array = shift_array(array=array, k=k)
    print(array)


if __name__ == '__main__':
    main()
