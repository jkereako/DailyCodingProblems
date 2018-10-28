import src
from src import problem_1
import unittest
import random

class TestProblem1(unittest.TestCase):
    def test_empty_list_is_none(self):
        result = problem_1.solution([], 42)
        
        self.assertIsNone(result)

    def test_single_element_list_is_none(self):
        result = problem_1.solution([2], 33)
        
        self.assertIsNone(result)

    def test_solution_is_in_simple_list(self):
        start = -3
        end = 10
        target_sum = 7

        result = problem_1.solution([end, start], target_sum)
        
        self.assertEqual(result[0], start)
        self.assertEqual(result[1], end)

    def test_solution_is_in_complex_list(self):
        L = [18, 15, 2, 21, 34, -13, 10, 0, -3, 21] 
        target_sum = 17

        result = problem_1.solution(L, target_sum)

        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 15)

    def test_solution_is_not_in_complex_list(self):
        L = [18, 15, 1, 29, 34, -13, 10, 0, -3, 21] 
        target_sum = 17

        result = problem_1.solution(L, target_sum)

        self.assertIsNone(result)