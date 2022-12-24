from typing import TypeAlias

AdjacencyList: TypeAlias = dict[str, set[str]]


def input_adjacency_list(*, count_edges: int) -> AdjacencyList:
    graph: AdjacencyList = {}

    for _ in range(count_edges):
        v1, v2 = input('Input vertices v1 v2: ').split()
        for v, u in (v1, v2), (v2, v1):
            if v not in graph:
                graph[v] = set()
            graph[v].add(u)

    return graph


def main() -> None:
    _ = int(input('Please input count vertices: '))
    count_edges = int(input('Please input count edges: '))
    adjacency_list = input_adjacency_list(count_edges=count_edges)
    print(adjacency_list)


if __name__ == '__main__':
    main()
