#url https://leetcode.com/problems/largest-perimeter-triangle/
#writtenby:anhty9le	

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        A.sort(reverse=True)
        print(A)
        for i in range(n-2):
            if A[i]<A[i+1]+A[i+2]: return A[i]+A[i+1]+A[i+2]
        return 0