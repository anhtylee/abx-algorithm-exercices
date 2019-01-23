# url https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# writtenby:anhty9le


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        for i in range(n):
            for j in range(i + 1, n):
                if A[i] == A[j]:
                    return A[i]
