# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the
# list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def solution(L, target_sum):
    # Sanity check
    if not L or len(L) < 2:
        return None

    # Sort the list such that we can find the solution in linear time.
    L.sort()
    
    start = 0
    end = 1

    for i in range(0, len(L)):
        if start == end:
            return None

        total = L[start] + L[-end]

        if total == target_sum:
            return (L[start], L[-end])
        elif total < target_sum:
            start += 1
        elif total > target_sum:
            end += 1
    
    return None
            