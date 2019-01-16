#url https://leetcode.com/problems/nim-game/
#writtenby:anhty9le	

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n)%4==0: return False
        else: return Tru