# url https://leetcode.com/problems/integer-break/
# writtenby:anhty9le


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 8:
            return (n / 2) * (n - n / 2)

        i = n // 3
        r = n - 3 * i

        if r == 2:
            return 3**i * 2

        return 3**(i - 1) * (3 + r)
