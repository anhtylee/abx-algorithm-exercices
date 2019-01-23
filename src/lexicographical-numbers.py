# url https://leetcode.com/problems/lexicographical-numbers/
# writtenby:anhty9le


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arrS = []
        arrI = []

        for i in range(1, n + 1):
            arrS.append(str(i))
        arrS.sort()

        for i in range(n):
            arrI.append(int(arrS[i]))

        return arrI
