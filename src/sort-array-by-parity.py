# url https://leetcode.com/problems/sort-array-by-parity
# writtenby:anhty9le


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        n = len(A)

        for i in range(n):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        return even + odd
