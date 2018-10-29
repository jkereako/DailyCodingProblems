# QUESTION:
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in 
# linear time and constant space. In other words, find the lowest positive
# integer that does not exist in the array. The array can contain duplicates
# and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
# should give 3.
#
# You can modify the input array in-place.

def solution(L):
    # Sanity check
    if not L:
        return None

    # Return the identity if the element-count is fewer than 2
    if len(L) <= 1:
        return L

    item_count = 0
    item_sum = 0

    for i in range(0, len(L)):
        # Throw away negative integers
        if L[i] < 0:
            continue

        item_sum += L[i]
        item_count += 1

    # If you don't know this trick then you won't be able to solve this in 
    # linear time.
    total = item_count * (item_count + 1) / 2

    return abs(total - item_sum)