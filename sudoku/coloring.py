"""Graph coloring algorithms."""

import networkx as nx
from math import sqrt


def welsh_powell(graph):
    """Runs the Welsh-Powell algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    def _welsh(graph):
        for node in graph.node:
            if not graph.node[node]['fixed']:
                for neighbor in graph.neighbors(node):
                    if (graph.node[neighbor]['fixed']):
                        try:
                            graph.node[node]['label'].remove(
                                graph.node[neighbor]['label'])
                        except:
                            pass

    def _update(graph):
        for node in graph.node:
            if (not graph.node[node]['fixed'] and
                    len(graph.node[node]['label']) == 1):
                graph.node[node]['fixed'] = True
                graph.node[node]['label'] = graph.node[node]['label'][0]

    def _clear(graph):
        for node in graph.node:
            if (graph.node[node]['fixed'] and
                    type(graph.node[node]['label']) is not int):
                graph.node[node]['fixed'] = False

    def _engage(graph):
        for i in range(size):
            for j in range(size):
                name = '{}{}'.format(i, j)
                if not graph.node[name]['fixed']:
                    graph.node[name]['fixed'] = True
                    _welsh(graph)
                    _update(graph)
        _clear(graph)

    size = int(sqrt(len(graph.node)))
    for node in graph.node:
        if (graph.node[node]['label'] is None):
            graph.node[node]['label'] = [(x + 1) for x in range(size)]

    for i in range(9):
        _engage(graph)
        _welsh(graph)
        _update(graph)

    return graph


def sequencial_coloring(graph):
    """Runs the Sequencial Coloring algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """

    def is_label_possible(graph, node, label):
        for neighbor in graph.neighbors(node):
            if graph.node[neighbor]['label'] == label:
                return False
        return True

    size = int(sqrt(len(graph.node)))
    labels = [(x + 1) for x in range(size)]
    for label in labels:
        for node in graph.node:
            if is_label_possible(graph, node, label):
                graph.node[node]['label'] = label
    return graph


def class_coloring(graph):
    """Runs the Class Coloring algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    raise NotImplementedError('')


def dsatur(graph):
    """Runs the Degree of Saturation heuristic algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    raise NotImplementedError('')
