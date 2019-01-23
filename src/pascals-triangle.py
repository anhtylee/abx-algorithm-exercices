# url https://leetcode.com/problems/pascals-triangle/
# writtenby:anhty9le


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows + 1
        arr = [[0 for i in range(n)]for j in range(n)]
        arr[0][0] = 1
        i = 1

        while i < n:
            for j in range(i):
                arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j])

            i += 1

        Result = [[1 for i in range(1)]for j in range(n - 1)]

        for i in range(1, n):
            for j in range(1, i):
                Result[i - 1].append(arr[i][j])

        return(Result)
