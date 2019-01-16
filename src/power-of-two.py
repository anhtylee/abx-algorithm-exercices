#url https://leetcode.com/problems/power-of-two
#writtenby:anhty9le	

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=1
        while a<n:
            a*=2
        if a==n: return True
        return False