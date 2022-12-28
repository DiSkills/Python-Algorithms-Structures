from src.graph.input.adjacency_matrix import input_adjacency_matrix


def test_input_adjacency_matrix(monkeypatch) -> None:
    # A - B - C - D
    inputs = iter(['A B', 'B C', 'C D']) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    graph = input_adjacency_matrix(count_vertices=4, count_edges=3)
    assert graph == [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
    ]

    # D - A - C
    # \   |   /
    #   - B -
    inputs = iter(['A B', 'B C', 'C A', 'D A', 'B D'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    graph = input_adjacency_matrix(count_vertices=4, count_edges=5)
    assert graph == [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
    ]
