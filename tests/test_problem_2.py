import src
from src import problem_2
import unittest
import random

class TestProblem2(unittest.TestCase):
    def test_empty_list_is_none(self):
        result = problem_2.solution([])
        
        self.assertIsNone(result)

    def test_two_element_list_is_identity(self):
        L = [2, 3]
        result = problem_2.solution(L)

        self.assertListEqual(result, L)

    def test_non_zero_list(self):
        L = [1, 2, 3, 4, 5]
        result = problem_2.solution(L)
        solution = [120, 60, 40, 30, 24]

        self.assertListEqual(result, solution)

    def test_zero_in_list(self):
        L = [1, 0, 2, 3, 4, 5]
        result = problem_2.solution(L)

        self.assertIsNone(result)
