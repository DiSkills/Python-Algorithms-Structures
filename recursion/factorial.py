def factorial(*, number: int) -> int:
    if number == 1:
        return 1
    return number * factorial(number=number - 1)


def main() -> None:
    print(factorial(number=5))


if __name__ == '__main__':
    main()
