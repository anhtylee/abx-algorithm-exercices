# url https://leetcode.com/problems/sort-array-by-parity-ii/
# writtenby:anhty9le


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        even = []
        odd = []

        for i in range(n):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        Result = []

        for i in range(n / 2):
            Result.append(even[i])
            Result.append(odd[i])

        return Result
