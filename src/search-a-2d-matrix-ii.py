#url https://leetcode.com/problems/search-a-2d-matrix-ii/
#writtenby:anhty9le	

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m=len(matrix)
        if m==0: return False
        n=len(matrix[0])
        if n==0: return False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]>=target:
                    if matrix[i][j]==target: return True
                    break
        
        return False
                    