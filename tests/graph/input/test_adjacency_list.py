from src.graph.input.adjacency_list import input_adjacency_list


def test_input_adjacency_list(monkeypatch) -> None:
    # A - B - C - D
    inputs = iter(['A B', 'B C', 'C D']) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    graph = input_adjacency_list(count_edges=3)
    assert graph == {
        'A': {'B'},
        'B': {'A', 'C'},
        'C': {'B', 'D'},
        'D': {'C'},
    }

    # D - A - C
    # \   |   /
    #   - B -
    inputs = iter(['A B', 'B C', 'C A', 'D A', 'B D'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    graph = input_adjacency_list(count_edges=5)
    assert graph == {
        'A': {'B', 'C', 'D'},
        'B': {'A', 'C', 'D'},
        'C': {'A', 'B'},
        'D': {'A', 'B'},
    }
