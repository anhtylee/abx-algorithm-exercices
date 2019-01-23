# url https://leetcode.com/problems/ugly-number/
# writtenby:anhty9le


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        n2 = int(round(math.pow(num, 1.0 / 2)))
        n3 = int(round(math.pow(num, 1.0 / 3)))
        n5 = int(round(math.pow(num, 1.0 / 5)))

        for i in range(n2 + 1):
            if math.pow(2, i) > num:
                break

            for j in range(n3 + 1):
                if math.pow(2, i) * math.pow(3, j) > num:
                    break

                for k in range(n5 + 1):
                    if math.pow(2, i) * math.pow(3, j) * math.pow(5, k) > num:
                        break

                    if math.pow(2, i) * math.pow(3, j) * math.pow(5, k) == num:
                        return True

        return False
