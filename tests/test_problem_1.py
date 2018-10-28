import src
from src import problem_1
import unittest
import random

class TestProblem1(unittest.TestCase):
    def test_empty_list_is_none(self):
      none = problem_1.solution([], 42)
      
      self.assertIsNone(none)

    def test_single_element_list_is_none(self):
      none = problem_1.solution([2], 33)
      
      self.assertIsNone(none)

    def test_solution_is_in_simple_list(self):
      start = -3
      end = 10
      target_sum = 7

      tuple = problem_1.solution([end, start], target_sum)
      
      self.assertEqual(tuple[0], start)
      self.assertEqual(tuple[1], end)

    def test_solution_is_in_complex_list(self):
      L = [18, 15, 2, 21, 34, -13, 10, 0, -3, 21] 
      target_sum = 17

      tuple = problem_1.solution(L, target_sum)

      self.assertEqual(tuple[0], 2)
      self.assertEqual(tuple[1], 15)

    def test_solution_is_not_in_complex_list(self):
      L = [18, 15, 1, 29, 34, -13, 10, 0, -3, 21] 
      target_sum = 17

      none = problem_1.solution(L, target_sum)

      self.assertIsNone(none)