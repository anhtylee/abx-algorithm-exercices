#url https://leetcode.com/problems/power-of-four/
#writtenby:anhty9le	

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=0
        while math.pow(4,i)<num:
            i+=1
        return math.pow(4,i)==num