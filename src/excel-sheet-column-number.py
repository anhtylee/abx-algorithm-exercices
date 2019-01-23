# url https://leetcode.com/problems/excel-sheet-column-number/
# writtenby:anhty9le


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        Result = 0

        for i in range(n):
            num = ord(s[i]) - 64
            Result += num * math.pow(26, n - i - 1)

        return int(Result)
