import unittest
import os.path
import sudoku.io
import sudoku.coloring


class ColoringTests(unittest.TestCase):

    def test_welsh_powell(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/9/sample-2.sdk')
        graph = sudoku.io.read(filepath)
        graph_solved = sudoku.coloring.welsh_powell(graph)

    def test_class_coloring(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/9/sample-2.sdk')
        graph = sudoku.io.read(filepath)
        graph_solved = sudoku.coloring.class_coloring(graph)

    def test_class_coloring_backtracking(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/9/sample-2.sdk')
        graph = sudoku.io.read(filepath)
        graph_solved = sudoku.coloring.class_coloring_backtracking(graph)

    def test_dsatur(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/9/sample-1.sdk')
        graph = sudoku.io.read(filepath)
        graph_solved = sudoku.coloring.dsatur(graph)

    def test_bfs_heuristic(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/9/sample-2.sdk')
        graph = sudoku.io.read(filepath)
        max_iterations = 100000
        graph_solved = sudoku.coloring.bfs_heuristic(graph,max_iterations)

    def test_dfs_heuristic(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/9/sample-2.sdk')
        graph = sudoku.io.read(filepath)
        max_iterations = 100000
        graph_solved = sudoku.coloring.dfs_heuristic(graph,max_iterations)
