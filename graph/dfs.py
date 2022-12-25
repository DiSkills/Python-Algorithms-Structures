from typing import TypeAlias

Graph: TypeAlias = dict[str, set[str]]


def dfs(*, vertex: str, graph: Graph, used: set[str]) -> None:
    used.add(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(vertex=neighbour, graph=graph, used=used)


def get_quantity_connectivity_components(graph: Graph) -> int:
    used: set[str] = set()
    quantity = 0
    for vertex in graph:
        if vertex not in used:
            dfs(vertex=vertex, graph=graph, used=used)
            quantity += 1
    return quantity


def main() -> None:
    graph: Graph = {
        '1': {'2', '3'},
        '2': {'1'},
        '3': {'1'},
        '4': {'5', '6'},
        '5': {'4'},
        '6': {'4'},
    }
    print(get_quantity_connectivity_components(graph=graph))


if __name__ == '__main__':
    main()
