from collections import deque


def is_seller(*, person: str) -> bool:
    return person == 'jonny'


def search(*, start: str, graph: dict[str, list[str]]) -> bool:
    queue = deque(graph[start])
    searched = set()
    while queue:
        person = queue.popleft()
        if person not in searched:
            if is_seller(person=person):
                print(f'Seller is {person}')
                return True
            queue += graph[person]
            searched.add(person)
    return False


def main() -> None:
    graph: dict[str, list[str]] = {
        'me': ['alice', 'bob', 'claire'],
        'bob': ['anuj', 'peggy'],
        'alice': ['peggy'],
        'claire': ['thom', 'jonny'],
        'anuj': [],
        'peggy': [],
        'thom': [],
        'jonny': [],
    }
    print(search(start='me', graph=graph))


if __name__ == '__main__':
    main()
