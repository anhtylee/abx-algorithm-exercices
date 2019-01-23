# url https://leetcode.com/problems/rotate-image
# writtenby:anhty9le


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        arr = [[[]for i in range(n)]for i in range(n)]

        for i in range(n):
            for j in range(n):
                arr[i][j] = matrix[j][i]

        for i in range(n):
            arr[i].reverse()

        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[i][j]
