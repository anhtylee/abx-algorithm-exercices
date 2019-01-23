# url https://leetcode.com/problems/valid-perfect-square/
# writtenby:anhty9le


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0

        while math.pow(i, 2) < num:
            i += 1

        return math.pow(i, 2) == num
