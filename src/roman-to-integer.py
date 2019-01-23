# url https://leetcode.com/problems/roman-to-integer/
# writtenby:anhty9le


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        arr = []
        year = 0

        for i in range(n):
            if s[i] == "I":
                k = 1
            elif s[i] == "V":
                k = 5
            elif s[i] == "X":
                k = 10
            elif s[i] == "L":
                k = 50
            elif s[i] == "C":
                k = 100
            elif s[i] == "D":
                k = 500
            elif s[i] == "M":
                k = 1000
            arr.append(k)

        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                year -= arr[i]
            else:
                year += arr[i]

        return year + arr[n - 1]
