#url https://leetcode.com/problems/jewels-and-stones/
#writtenby:anhty9le	

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        k=0;
        for i in  range(len(J)):
            for j in range(len(S)):
                if J[i]==S[j]: k+=1
        return k
