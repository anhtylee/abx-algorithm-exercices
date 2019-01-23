# url https://leetcode.com/problems/fibonacci-number/
# writtenby:anhty9le


def F(N):
    if N == 0:
        return 0

    if N == 1:
        return 1

    return F(N - 1) + F(N - 2)


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        return F(N)
