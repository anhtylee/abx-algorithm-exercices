#url https://leetcode.com/problems/1-bit-and-2-bit-characters/
#writtenby:anhty9le	

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i=0
        n=len(bits)
        while i<n:
            if bits[i]==0:
                i+=1
                check=True
            else: 
                i+=2
                check=False
        return check
        