import src
from src import problem_5
import unittest
import random

class TestProblem5(unittest.TestCase):
    def setUp(self):
        self.cons = problem_5.cons(3, 4)
        self.car = problem_5.car
        self.cdr = problem_5.cdr

    def test_car(self):
        result = self.cons(self.car)
        
        self.assertEqual(3, result)

    def test_cdr(self):
        result = self.cons(self.cdr)
        
        self.assertEqual(4, result)
