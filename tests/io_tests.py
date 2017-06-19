import unittest
import os.path
import sudoku.io
import networkx as nx
import matplotlib.pyplot as plt

class IoTests(unittest.TestCase):

    def test_read(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        graph = sudoku.io.read(filepath)


    def test_read_draw(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        graph = sudoku.io.read(filepath)
        nx.draw_circular(graph)
        plt.show()


    def test_read_adjacents(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        graph = sudoku.io.read(filepath)
        nodes_degree = [len(graph.neighbors(n)) for n in graph.node]
        print(nodes_degree[0])
        print(all([d == nodes_degree[0] for d in nodes_degree]))


    def test_write(self):
        raise NotImplementedError('')
