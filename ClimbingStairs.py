# 70. Climbing Stairs  QuestionEditorial Solution

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n    = 0, 1, 2, 3, 4, 5, ...
        # f(n) = 1, 1, 2, 3, 5, 8, ...
        # f(n) = f(n-2) + f(n-1)
        # Time ~ O(n)
        a = b = 1
        for i in range(n):
            a, b = b, a+b
        return a
