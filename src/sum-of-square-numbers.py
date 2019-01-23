# url https://leetcode.com/problems/sum-of-square-numbers/
# writtenby:anhty9le


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0

        while i**2 <= c:
            j = c - i**2
            if math.sqrt(j) == int(round(math.sqrt(j))):
                return True
            i += 1

        return False
