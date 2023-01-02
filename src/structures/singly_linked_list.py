class Node:
    def __init__(self, *, data: int) -> None:
        self.data = data
        self.next: Node | None = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._length = 0

    def append(self, data: int) -> None:
        node = Node(data=data)
        if self.head is None:
            self.head = node
        elif self.tail is not None:
            self.tail.next = node
        self.tail = node
        self._length += 1

    def __len__(self) -> int:
        return self._length
