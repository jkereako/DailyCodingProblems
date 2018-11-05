import src
from src import problem_4
import unittest
import random

class TestProblem4(unittest.TestCase):
    def test_empty_list_is_none(self):
        result = problem_4.solution([])
        
        self.assertIsNone(result)

    def test_one_element_list_is_identity(self):
        L = [89]
        result = problem_4.solution(L)

        self.assertListEqual(result, L)
    
    # def test_two_element_list(self):
    #     L = [3, 5]
    #     result = problem_4.solution(L)
    #     solution = 4
        
    #     self.assertEqual(result, solution)

    def test_negative_integer_list(self):
        L = [3, 4, -1, 1]
        result = problem_4.solution(L)
        solution = 2
        
        self.assertEqual(result, solution)
