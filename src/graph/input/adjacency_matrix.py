from typing import TypeAlias

AdjacencyMatrix: TypeAlias = list[list[int]]


def input_adjacency_matrix(
    *, count_vertices: int, count_edges: int,
) -> AdjacencyMatrix:
    vertices: list[str] = []
    indexes: dict[str, int] = {}
    adjacency_matrix: AdjacencyMatrix = [
        [0] * count_vertices for _ in range(count_vertices)
    ]

    for _ in range(count_edges):
        v1, v2 = input('Input vertices v1 v2: ').split()

        for vertex in v1, v2:
            if vertex not in indexes:
                vertices.append(vertex)
                indexes[vertex] = len(vertices) - 1

        v1_index, v2_index = indexes[v1], indexes[v2]
        adjacency_matrix[v1_index][v2_index] += 1
        adjacency_matrix[v2_index][v1_index] += 1

    return adjacency_matrix


def main() -> None:
    count_vertices = int(input('Please input count vertices: '))
    count_edges = int(input('Please input count edges: '))
    adjacency_matrix = input_adjacency_matrix(
        count_vertices=count_vertices, count_edges=count_edges,
    )
    print(adjacency_matrix)


if __name__ == '__main__':
    main()
