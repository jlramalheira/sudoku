"""Functions that check the validity of a sudoku instance."""


def is_solved(graph):
    """Returns True if the graph represents a valid sudoku instance.

    Arguments:
        graph (networkx.Graph): The sudoku instance.
    """
    if not is_full(graph):
        return False
    else:
        for node in graph.node:
            label = graph.node[node]['label']
            for neighbor in graph.neighbors(node):
                if graph.node[neighbor]['label'] == label:
                    return False
        return True


def is_full(graph):
    """Returns True if the graph represents a full sudoku instance.

    Arguments:
        graph (networkx.Graph): The sudoku instance.
    """
    for node in graph.node:
        if type(graph.node[node]['label']) is not int:
            return False
    return True
