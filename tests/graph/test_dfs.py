from src.graph.dfs import get_quantity_connectivity_components


def test_get_quantity_connectivity_components() -> None:
    # A - B - C - D
    graph: dict[str, set[str]] = {
        'A': {'B'},
        'B': {'A', 'C'},
        'C': {'B', 'D'},
        'D': {'C'},
    }
    quantity = get_quantity_connectivity_components(graph=graph)
    assert quantity == 1

    # A - B
    # \   /
    #   C   .D
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'C'},
        'C': {'A', 'B'},
        'D': set(),
    }
    quantity = get_quantity_connectivity_components(graph=graph)
    assert quantity == 2
