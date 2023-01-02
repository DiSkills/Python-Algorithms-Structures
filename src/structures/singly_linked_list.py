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

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        data: list[str] = []
        node = self.head
        while node is not None:
            data.append(str(node.data))
            node = node.next
        data.append('None')
        return ' -> '.join(data)

    def append(self, data: int) -> None:
        node = Node(data=data)
        if self.head is None:
            self.head = node
        elif self.tail is not None:
            self.tail.next = node
        self.tail = node
        self._length += 1
