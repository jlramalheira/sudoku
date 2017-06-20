import unittest
import os.path
import sudoku.checking
import sudoku.io


class CheckingTests(unittest.TestCase):

    def is_full_test(self):
        full_filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/solved-1.sdk')
        full_graph = sudoku.io.read(full_filepath)
        self.assertTrue(sudoku.checking.is_full(full_graph))
        not_full_filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        not_full_graph = sudoku.io.read(not_full_filepath)
        self.assertFalse(sudoku.checking.is_full(not_full_graph))

    def is_solved_test(self):
        solved_filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/solved-1.sdk')
        solved = sudoku.io.read(solved_filepath)
        self.assertTrue(sudoku.checking.is_solved(solved))
        unsolved_filepath = os.path.join(
            os.path.dirname(__file__),
            '../rsc/sample-1.sdk')
        unsolved = sudoku.io.read(unsolved_filepath)
        self.assertFalse(sudoku.checking.is_solved(unsolved))
