# url https://leetcode.com/problems/find-the-difference/
# writtenby:anhty9le


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        n = len(s)
        arrS = []
        arrT = []

        for i in range(n):
            arrS.append(s[i])
            arrT.append(t[i])

        arrT.append(t[n])
        arrS.sort()
        arrT.sort()
        arrS.append("0")

        for i in range(n + 1):
            if arrS[i] != arrT[i]:
                return arrT[i]
