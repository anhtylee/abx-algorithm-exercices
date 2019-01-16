#url https://leetcode.com/problems/range-addition-ii/
#writtenby:anhty9le	

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        row=m
        col=n
        
        for i in range(len(ops)):
            if row>ops[i][0]: row=ops[i][0]
            if col>ops[i][1]: col=ops[i][1]
        return row*col