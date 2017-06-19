"""IO operations of a serialized form of a Sudoku."""

from os import path
from math import sqrt
import networkx as nx


def read(filepath):
    """Returns a networkx.Graph that represents a sudoku readed from file.

    Arguments:
        filepath (str): the path of the file.
    Returns:
        A networkx.Graph object representation of the sudoku.
    """
    if path.exists(filepath):
        lines = []
        with open(filepath, 'r') as sudoku_file:
            lines = [l.rstrip('\n') for l in sudoku_file.readlines()]
        if (sqrt(len(lines)) % 1) != 0:
            raise IOError('The file path doesn\'t represents a sudoku game.')
        elements = [[int(e) for e in l.split(' ')] for l in lines]
        return _build_sudoku_instance_graph(elements)
    else:
        raise IOError('The file of the path doesn\'t exists.')


def persist(filepath, sudoku):
    """Persists a sudoku instance in a file.

    Arguments:
        filepath (str): the path of the file.
        sudoku (networkx.Graph): the graph representation of the sudoku.
    """
    raise NotImplementedError('')


def _build_sudoku_instance_graph(elements):
    """Creates a graph representation of a sudoku instance.

    Arguments:
        elements (list[list[int]]): A matrix representation of the sudoku instance.
    Returns:
        A networkx.Graph object representation of the sudoku instance.
    """
    size = len(elements)
    graph = nx.Graph()
    (rowcols, regions) = _get_named_elements(size)
    for i in range(size):
        for j in range(size):
            value = elements[i][j]
            if value != 0:
                graph.add_node(rowcols[i][j], label=value, fixed=True)
            else:
                graph.add_node(rowcols[i][j], label=None, fixed=False)
    # edges for rows
    for i in range(size):
        for j in range(size - 1):
            for k in range(j, size - 1):
                graph.add_edge(rowcols[i][j], rowcols[i][k + 1])
    # edges for cols
    for i in range(size - 1):
        for j in range(size):
            for k in range(i, size - 1):
                graph.add_edge(rowcols[i][j], rowcols[k + 1][j])
    # edges for regions
    for i in range(size):
        for j in range(size - 1):
            for k in range(j, size - 1):
                graph.add_edge(regions[i][j], regions[i][k + 1])
    return graph


def _get_named_elements(size):
    """Returns the sudoku n-sized named elements (rows-cols and regions).

    Arguments:
        size (int): The size of the sudoku instance.
    Returns:
        A tuple (rowscols, regions) where:
            rowscols (list[list[str]]): named elements of the a row and a col.
            regions (list[list[str]]): named elements of a region.
    """
    order = int(sqrt(size))
    rowcols = [
        [str(i) + str(j)
         for j in range(size)]
        for i in range(size)]
    regions = [
        [str(i // order * order + j // order) + str(j % order + i % order * order)
         for j in range(size)]
        for i in range(size)]
    return (rowcols, regions)
