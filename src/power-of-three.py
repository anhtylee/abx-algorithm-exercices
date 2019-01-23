# url https://leetcode.com/problems/power-of-three/
# writtenby:anhty9le


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = 1

        while a < n:
            a *= 3

        if a == n:
            return True

        return False
