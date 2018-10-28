# QUESTION:
#
# This problem was asked by Uber.
# 
# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the original 
# array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
# be [2, 3, 6].
# 
# Follow-up: what if you can't use division?

from functools import reduce

def solution(L):
    # Sanity check
    if not L:
        return None

    # Return the identity if the element-count is fewer than 3
    if len(L) < 3:
      return L

    # Prevent division-by-zero
    for i in range(0, len(L)):
      if L[i] == 0:
        return None

    product = 1

    multiply = lambda x, y: x * y
    divide = lambda x: product // x

    product = reduce(multiply, L)

    return list(map(divide, L))
            