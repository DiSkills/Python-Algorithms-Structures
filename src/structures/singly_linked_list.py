from typing import Iterator


class Node:
    def __init__(self, *, data: int) -> None:
        self.data = data
        self.next: Node | None = None

    def __repr__(self) -> str:
        return str(self.data)

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def _add_start_data(self, *, data: list[int] | None = None) -> None:
        if data is None:
            return

        for item in data:
            self.push_back(item)

    def __init__(self, *, data: list[int] | None = None) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._length = 0

        self._add_start_data(data=data)

    @property
    def head(self) -> int | None:
        return None if self._head is None else self._head.data

    @property
    def tail(self) -> int | None:
        return None if self._tail is None else self._tail.data

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        data: list[str] = [str(node) for node in self.__iter__()]
        data.append('None')
        return ' -> '.join(data)

    def __iter__(self) -> Iterator[Node]:
        node = self._head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, index: int) -> int | None:
        node = self._get_node(index=index)
        return None if node is None else node.data

    def _get_node(self, index: int) -> Node | None:
        if self._head is None:
            raise IndexError('SinglyLinkedList is empty')

        length = len(self)
        if not (-length <= index < length):
            raise IndexError(f'Node not found with index: {index}')
        index = (index + length) % length

        i = 0
        node: Node | None = self._head
        while (node is not None) and (i < index):
            node = node.next
            i += 1
        return node

    def push_front(self, data: int) -> None:
        node = Node(data=data)
        node.next = self._head
        self._head = node
        if self._tail is None:
            self._tail = node
        self._length += 1

    def push_back(self, data: int) -> None:
        node = Node(data=data)
        if self._head is None:
            self._head = node
        elif self._tail is not None:
            self._tail.next = node
        self._tail = node
        self._length += 1

    def pop_front(self) -> None:
        if self._head is None:
            raise IndexError('SinglyLinkedList is empty')
        elif self._head == self._tail:
            self._tail = None
        self._head = self._head.next
        self._length -= 1

    def pop_back(self) -> None:
        if self._tail is None:
            raise IndexError('SinglyLinkedList is empty')
        elif self._head == self._tail:
            self._head = None

        try:
            node = self._get_node(index=-2)
        except IndexError:
            node = None

        if node is not None:
            node.next = None
        self._tail = node
        self._length -= 1
