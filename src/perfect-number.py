# url https://leetcode.com/problems/perfect-number/
# writtenby:anhty9le


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False

        n = int(round(math.sqrt(num))) + 1

        sum = 0

        for i in range(2, n):
            if num % i == 0:
                sum += i + num // i

        return sum + 1 == num
