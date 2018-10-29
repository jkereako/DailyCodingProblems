# QUESTION:
#
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes
# the tree into a string, and deserialize(s), which deserializes the string
# back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
            