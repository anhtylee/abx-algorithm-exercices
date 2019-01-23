# url https://leetcode.com/problems/toeplitz-matrix/
# writtenby:anhty9le


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i + 1][j + 1] != matrix[i][j]:
                    return False

        return True
