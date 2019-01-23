# url https://leetcode.com/problems/monotonic-array/
# writtenby:anhty9le


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        n = len(A)

        while i < n - 1 and A[i] == A[i + 1]:
            i += 1

        if i == n - 1:
            return True

        k = A[i] - A[i + 1]

        if k > 0:
            for i in range(n - 1):
                if A[i] < A[i + 1]:
                    return False

        if k < 0:
            for i in range(n - 1):
                if A[i] > A[i + 1]:
                    return False

        return True
