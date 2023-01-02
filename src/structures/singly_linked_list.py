from typing import Iterator


class Node:
    def __init__(self, *, data: int) -> None:
        self.data = data
        self.next: Node | None = None

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.data == other.data


class LinkedList:
    def _add_start_data(self, *, data: list[int] | None = None) -> None:
        if data is None:
            return

        for item in data:
            self.append(item)

    def __init__(self, *, data: list[int] | None = None) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._length = 0

        self._add_start_data(data=data)

    @property
    def head(self) -> Node | None:
        return self._head

    @property
    def tail(self) -> Node | None:
        return self._tail

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        data: list[str] = []
        node = self._head
        while node is not None:
            data.append(str(node.data))
            node = node.next
        data.append('None')
        return ' -> '.join(data)

    def __iter__(self) -> Iterator[Node]:
        node = self._head
        while node is not None:
            yield node
            node = node.next

    def append_left(self, data: int) -> None:
        node = Node(data=data)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._length += 1

    def append(self, data: int) -> None:
        node = Node(data=data)
        if self._head is None:
            self._head = node
        elif self._tail is not None:
            self._tail.next = node
        self._tail = node
        self._length += 1
