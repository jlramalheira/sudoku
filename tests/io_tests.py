import unittest
import os.path
import math
import sudoku.io
import networkx as nx
import matplotlib.pyplot as plt

class IoTests(unittest.TestCase):

    def test_read(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        graph = sudoku.io.read(filepath)
        order = int(math.pow(len(graph.node), 1 / 4))
        node_degree = (3 * (order ** 2)) - (2 * (order - 1)) - 3
        nodes_degree = [len(graph.neighbors(n)) for n in graph.node]
        self.assertTrue(
            expr=all([d == nodes_degree[0] for d in nodes_degree]),
            msg='All vertexes must have the same degree.')
        self.assertTrue(
            expr=nodes_degree[0] == node_degree,
            msg='The vertex degree must be')

    def test_read_draw(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        nx.draw_circular(graph)
        graph = sudoku.io.read(filepath)
        plt.show()

    def test_write(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        graph = sudoku.io.read(filepath)
        sudoku.io.print(graph)
