#url https://leetcode.com/problems/reverse-integer/
#writtenby:anhty9le	

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign=1
        if x<0:
            sign=-1
            x=abs(x)
        s=str(x)
        s=s[::-1]
        
        if int(s)>math.pow(2,31): return 0
        
        return sign*int(s)